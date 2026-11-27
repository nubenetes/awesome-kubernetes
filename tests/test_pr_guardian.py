import asyncio
import json
import unittest
from unittest.mock import patch

import httpx

from src.pr_guardian import (
    classify_pr_actor,
    parse_and_validate_external_diff,
    validate_dependabot_pr,
    validate_maintainer_pr,
    validate_mkdocs_config_content,
    verify_semantic_placement,
    verify_url_and_extract_ground_truth,
)


SAMPLE_AZURE_DOC = """# Azure

## Table of Contents

1. [Azure AD and RBAC](#azure-ad-and-rbac)
2. [AKS Networking](#aks-networking)

## Azure AD and RBAC

- [Azure Workload Identity Overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) - Official Microsoft guide to federating Kubernetes service accounts with Entra ID.
- [Azure RBAC for Kubernetes Authorization](https://learn.microsoft.com/en-us/azure/aks/manage-azure-rbac) - Unified role-based access control across Azure ARM and AKS API server.
- **(2026)** [Managed Identity vs Service Principal Deep Dive](https://azure.github.io/identity-guide/managed-identities) - Architectural comparison of token lifecycle, rotation, and blast radius for AKS workloads.
"""


class TestPRGuardianGates(unittest.TestCase):
    def test_actor_classification_blocks_fork_impersonation(self):
        self.assertEqual(
            classify_pr_actor("inafev", "nubenetes/awesome-kubernetes", "feat/new-hub"),
            "maintainer",
        )
        self.assertEqual(
            classify_pr_actor("dependabot[bot]", "nubenetes/awesome-kubernetes", "dependabot/pip/httpx"),
            "dependabot",
        )
        # Fork attempting to spoof internal bot/* branch name must be classified as external
        self.assertEqual(
            classify_pr_actor("mallory", "mallory/awesome-kubernetes", "bot/knowledge-update-123"),
            "external",
        )
        self.assertEqual(
            classify_pr_actor("amareswer", "amareswer/awesome-kubernetes", "add-azure-guide"),
            "external",
        )

    def test_gate1_accepts_clean_external_v1_link_addition_and_extracts_context(self):
        patch_txt = (
            "@@ -9,2 +9,3 @@\n"
            " - [Azure Workload Identity Overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) - Official Microsoft guide.\n"
            " - [Azure RBAC for Kubernetes Authorization](https://learn.microsoft.com/en-us/azure/aks/manage-azure-rbac) - Unified RBAC.\n"
            "+- **(2026)** [Managed Identity vs Service Principal Deep Dive](https://azure.github.io/identity-guide/managed-identities) - Architectural comparison of token lifecycle, rotation, and blast radius for AKS workloads.\n"
        )
        files = [{"filename": "docs/azure.md", "status": "modified", "patch": patch_txt}]
        ok, reasons, candidates = parse_and_validate_external_diff(
            files,
            get_head_file_fn=lambda _: SAMPLE_AZURE_DOC,
            get_base_existing_urls_fn=lambda _: {
                "https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview",
                "https://learn.microsoft.com/en-us/azure/aks/manage-azure-rbac",
            },
        )
        self.assertTrue(ok, f"Expected clean external V1 link addition to pass Gate 1, got: {reasons}")
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["section_path"], "Azure AD and RBAC")
        self.assertEqual(candidates[0]["h1_title"], "Azure")
        self.assertGreaterEqual(len(candidates[0]["siblings"]), 2)

    def test_gate1_handles_eof_newline_normalization_gracefully(self):
        patch_txt = (
            "@@ -10,1 +10,2 @@\n"
            "-- [Existing Tool](https://example.com/existing) - Existing valid curated description.\n"
            "\\ No newline at end of file\n"
            "+- [Existing Tool](https://example.com/existing) - Existing valid curated description.\n"
            "+- [New K8s Tool](https://example.com/new-k8s-tool) - Declarative drift detector for Kubernetes manifests.\n"
        )
        files = [{"filename": "docs/kubernetes-tools.md", "status": "modified", "patch": patch_txt}]
        ok, reasons, candidates = parse_and_validate_external_diff(
            files,
            get_head_file_fn=lambda _: "# Kubernetes Tools\n\n## CLI Tools\n\n- [Existing Tool](https://example.com/existing) - Existing.\n- [New K8s Tool](https://example.com/new-k8s-tool) - Declarative drift detector.\n",
            get_base_existing_urls_fn=lambda _: {"https://example.com/existing"},
        )
        self.assertTrue(ok, f"EOF newline normalization should not be treated as deletion: {reasons}")
        self.assertEqual(len(candidates), 1)

    def test_gate1_holds_v2_docs_infrastructure_and_protected_files(self):
        for bad_path in (
            "v2-docs/kubernetes.md",
            ".github/workflows/07.1.pr_guardian.yml",
            "src/pr_guardian.py",
            "mkdocs.yml",
            "README.md",
            "docs/index.md",
            "docs/about.md",
        ):
            files = [
                {
                    "filename": bad_path,
                    "status": "modified",
                    "patch": "@@ -1,1 +1,2 @@\n+- [Tool](https://example.com/tool) - High-density summary for testing.\n",
                }
            ]
            ok, reasons, _ = parse_and_validate_external_diff(
                files, get_head_file_fn=lambda _: "", get_base_existing_urls_fn=lambda _: set()
            )
            self.assertFalse(ok, f"External edit to {bad_path} MUST be held")
            self.assertGreater(len(reasons), 0)

    def test_gate1_holds_heading_changes_deletions_shorteners_and_trackers(self):
        # 1. Adding a new ## section heading
        heading_files = [
            {
                "filename": "docs/azure.md",
                "status": "modified",
                "patch": "@@ -10,1 +10,3 @@\n+## New Unauthorized Section\n+- [Tool](https://example.com/a) - Detailed technical description of tool.\n",
            }
        ]
        ok, reasons, _ = parse_and_validate_external_diff(
            heading_files, get_head_file_fn=lambda _: SAMPLE_AZURE_DOC, get_base_existing_urls_fn=lambda _: set()
        )
        self.assertFalse(ok)
        self.assertTrue(any("heading" in r.lower() for r in reasons))

        # 2. Deleting an existing curated link
        del_files = [
            {
                "filename": "docs/azure.md",
                "status": "modified",
                "patch": "@@ -9,2 +9,1 @@\n-- [Old Gem](https://example.com/gem) 🌟 - Sacred manual note.\n+- [New Tool](https://example.com/new) - Detailed replacement summary text.\n",
            }
        ]
        ok, reasons, _ = parse_and_validate_external_diff(
            del_files, get_head_file_fn=lambda _: SAMPLE_AZURE_DOC, get_base_existing_urls_fn=lambda _: set()
        )
        self.assertFalse(ok)
        self.assertTrue(any("existing curated" in r.lower() for r in reasons))

        # 3. URL shortener & UTM tracker
        for bad_url in ("https://bit.ly/3xyz123", "https://example.com/guide?utm_source=twitter"):
            bad_files = [
                {
                    "filename": "docs/azure.md",
                    "status": "modified",
                    "patch": f"@@ -9,1 +9,2 @@\n+- [Guide]({bad_url}) - Comprehensive architectural guide for AKS.\n",
                }
            ]
            ok, _, _ = parse_and_validate_external_diff(
                bad_files, get_head_file_fn=lambda _: SAMPLE_AZURE_DOC, get_base_existing_urls_fn=lambda _: set()
            )
            self.assertFalse(ok, f"Expected bad URL {bad_url} to be rejected in Gate 1")

    def test_maintainer_and_dependabot_guards(self):
        # Clean URLs check blocks offline plugin or missing use_directory_urls
        self.assertEqual(validate_mkdocs_config_content("mkdocs.yml", "use_directory_urls: true\nplugins:\n  - search\n"), [])
        self.assertTrue(validate_mkdocs_config_content("mkdocs.yml", "use_directory_urls: false\n"))
        self.assertTrue(validate_mkdocs_config_content("v2-mkdocs.yml", "use_directory_urls: true\nplugins:\n  - offline\n"))

        ok_dep, _ = validate_dependabot_pr(
            "chore(deps): bump httpx from 0.27.0 to 0.27.2",
            [{"filename": "requirements.txt", "status": "modified"}],
        )
        self.assertTrue(ok_dep)

        ok_major, reasons_major = validate_dependabot_pr(
            "chore(deps): bump actions/checkout from 6 to 7",
            [{"filename": ".github/workflows/06.deploy_final.yml", "status": "modified"}],
        )
        self.assertFalse(ok_major)
        self.assertTrue(any("major" in r.lower() for r in reasons_major))

        ok_maint, reasons_maint = validate_maintainer_pr(
            [{"filename": "docs/azure.md", "status": "modified", "patch": "+<script src='https://evil.example/x.js'></script>"}],
            get_file_content_fn=lambda _: "",
        )
        self.assertFalse(ok_maint)
        self.assertTrue(any("script" in r.lower() for r in reasons_maint))

    def test_gate2_live_url_and_github_mvq_verification(self):
        def handler(request: httpx.Request) -> httpx.Response:
            u = str(request.url)
            if u == "https://api.github.com/repos/org/active-tool":
                return httpx.Response(
                    200,
                    json={
                        "archived": False,
                        "disabled": False,
                        "stargazers_count": 420,
                        "pushed_at": "2026-10-15T10:00:00Z",
                        "topics": ["kubernetes", "ebpf"],
                        "license": {"spdx_id": "Apache-2.0"},
                        "description": "eBPF Kubernetes network policy verifier",
                    },
                )
            if u == "https://github.com/org/active-tool":
                return httpx.Response(
                    200,
                    headers={"content-type": "text/html"},
                    text="<html><head><title>org/active-tool: eBPF K8s</title></head><body>Active repo</body></html>",
                )
            if u == "https://api.github.com/repos/org/stale-tool":
                return httpx.Response(
                    200,
                    json={
                        "archived": False,
                        "disabled": False,
                        "stargazers_count": 12,
                        "pushed_at": "2019-01-01T00:00:00Z",
                        "license": {"spdx_id": "MIT"},
                    },
                )
            if u == "https://api.github.com/repos/org/bsl-tool":
                return httpx.Response(
                    200,
                    json={
                        "archived": False,
                        "disabled": False,
                        "stargazers_count": 900,
                        "pushed_at": "2026-11-01T00:00:00Z",
                        "license": {"spdx_id": "BUSL-1.1"},
                    },
                )
            return httpx.Response(404, text="Not Found")

        async def run_checks():
            transport = httpx.MockTransport(handler)
            async with httpx.AsyncClient(transport=transport, follow_redirects=True) as client:
                ok_good, _, gt = await verify_url_and_extract_ground_truth(
                    "https://github.com/org/active-tool", gh_token="fake", http_client=client
                )
                self.assertTrue(ok_good)
                self.assertEqual(gt["gh_stars"], 420)
                self.assertIn("kubernetes", gt["gh_topics"])

                ok_stale, msg_stale, _ = await verify_url_and_extract_ground_truth(
                    "https://github.com/org/stale-tool", gh_token="fake", http_client=client
                )
                self.assertFalse(ok_stale)
                self.assertIn("4 years", msg_stale)

                ok_bsl, msg_bsl, _ = await verify_url_and_extract_ground_truth(
                    "https://github.com/org/bsl-tool", gh_token="fake", http_client=client
                )
                self.assertFalse(ok_bsl)
                self.assertIn("BUSL-1.1", msg_bsl)

                ok_404, _, _ = await verify_url_and_extract_ground_truth(
                    "https://example.com/missing-doc", http_client=client
                )
                self.assertFalse(ok_404)

        asyncio.run(run_checks())

    def test_gate3_semantic_placement_pass_mismatch_and_fail_closed(self):
        sample_candidates = [
            {
                "file": "docs/azure.md",
                "h1_title": "Azure",
                "section_path": "Azure AD and RBAC",
                "siblings": ["- [Azure Workload Identity](https://learn.microsoft.com/aks) - Guide."],
                "title": "AKS Managed Identity Guide",
                "url": "https://azure.github.io/identity-guide",
                "description": "Deep dive into AKS managed identities vs service principals.",
                "ground_truth": {
                    "final_url": "https://azure.github.io/identity-guide",
                    "page_title": "AKS Managed Identity vs Service Principal",
                    "meta_description": "Technical guide for Entra ID and RBAC on AKS.",
                },
            }
        ]

        async def run_gate3():
            # 1. High-confidence match via €0.00 GitHub Models tier
            with patch(
                "src.pr_guardian._call_github_models_free",
                return_value=[
                    {
                        "index": 0,
                        "is_valid_technical_resource": True,
                        "url_matches_claimed_topic": True,
                        "fits_target_file_and_section": True,
                        "confidence": 0.94,
                        "suggested_category_file": "",
                        "reason": "Directly covers Entra ID managed identities on Azure AKS.",
                    }
                ],
            ):
                ok, reasons, verdicts, provider = await verify_semantic_placement(sample_candidates)
                self.assertTrue(ok, f"Expected pass, got {reasons}")
                self.assertEqual(provider, "GitHub Models (€0.00)")
                self.assertTrue(verdicts[0]["passed"])

            # 2. Category mismatch -> held with suggested category
            with patch(
                "src.pr_guardian._call_github_models_free",
                return_value=[
                    {
                        "index": 0,
                        "is_valid_technical_resource": True,
                        "url_matches_claimed_topic": True,
                        "fits_target_file_and_section": False,
                        "confidence": 0.91,
                        "suggested_category_file": "docs/finops.md",
                        "reason": "Resource is a FinOps billing calculator unrelated to Azure AD RBAC.",
                    }
                ],
            ):
                ok, reasons, _, _ = await verify_semantic_placement(sample_candidates)
                self.assertFalse(ok)
                self.assertTrue(any("docs/finops.md" in r for r in reasons))

            # 3. Fail-closed when all AI providers are unavailable
            with patch("src.pr_guardian._call_github_models_free", return_value=None), patch(
                "src.pr_guardian._call_gemini_free_key", return_value=None
            ), patch("src.pr_guardian.call_gemini_with_retry", side_effect=RuntimeError("offline")):
                ok, reasons, _, _ = await verify_semantic_placement(sample_candidates)
                self.assertFalse(ok)
                self.assertTrue(any("fail-closed" in r.lower() for r in reasons))

        asyncio.run(run_gate3())


if __name__ == "__main__":
    unittest.main()
