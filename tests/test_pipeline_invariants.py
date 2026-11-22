import json
import os
import re
import unittest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestPipelineInvariants(unittest.TestCase):
    """Guardrails enforcing zero-token publishing, Mandate 11 sync, category consistency, OKF v0.3, and parser safety."""

    def test_mandate_11_curation_sources_synced_with_workflow_ui(self):
        sources_path = os.path.join(REPO_ROOT, "data/curation_sources.yaml")
        workflow_path = os.path.join(REPO_ROOT, ".github/workflows/01.1.agentic_cron.yml")
        with open(sources_path, "r", encoding="utf-8") as f:
            sources = yaml.safe_load(f).get("sources", [])
        with open(workflow_path, "r", encoding="utf-8") as f:
            workflow_text = f.read()

        for entry in sources:
            topic = entry["topic"]
            self.assertIn(
                topic,
                workflow_text,
                f"Mandate 11 violation: topic '{topic}' missing from 01.1.agentic_cron.yml",
            )

        wf_yaml = yaml.safe_load(workflow_text)
        triggers = wf_yaml.get(True, wf_yaml.get("on", {}))
        dispatch_inputs = triggers.get("workflow_dispatch", {}).get("inputs", {})
        self.assertLessEqual(
            len(dispatch_inputs),
            25,
            f"01.1.agentic_cron.yml has {len(dispatch_inputs)} workflow_dispatch inputs (GitHub limit is 25)",
        )

    def test_v2_publisher_is_strictly_zero_ai_token(self):
        pub_path = os.path.join(REPO_ROOT, ".github/workflows/04.1.agentic_v2_publish.yml")
        with open(pub_path, "r", encoding="utf-8") as f:
            pub_text = f.read()
        self.assertNotIn("GEMINI_API_KEY", pub_text, "04.1. V2 Publisher must remain strictly 0-AI-token")
        self.assertNotIn("src.news_digest", pub_text, "src.news_digest belongs exclusively in 09. Weekly Digest")

    def test_v2_ai_curator_does_not_trigger_on_push(self):
        ai_path = os.path.join(REPO_ROOT, ".github/workflows/03.2.agentic_v2_ai.yml")
        with open(ai_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        triggers = data.get(True, data.get("on", {}))
        self.assertNotIn("push", triggers, "03.2. V2 AI Curator must not fire on master pushes")

    def test_deploy_workflow_enables_social_card_imaging(self):
        deploy_path = os.path.join(REPO_ROOT, ".github/workflows/06.deploy_final.yml")
        with open(deploy_path, "r", encoding="utf-8") as f:
            txt = f.read()
        self.assertIn("mkdocs-material[imaging]", txt)
        self.assertIn("libcairo2-dev", txt)

    def test_new_hubs_and_display_names_consistent_across_pipeline(self):
        from src.config import NUBENETES_CATEGORIES
        from src.fast_enrich import DIMENSIONS as FAST_DIMS, get_readable_category
        from src.news_digest import NewsDigestEngine

        for slug, expected_title in [("ocp5", "OCP 5"), ("ai-rag-okf", "AI RAG & OKF")]:
            self.assertIn(slug, NUBENETES_CATEGORIES)
            self.assertEqual(get_readable_category(slug), expected_title)
            self.assertTrue(any(slug in cats for cats in FAST_DIMS.values()))
            self.assertTrue(any(slug in cats for cats in NewsDigestEngine.DIGEST_CATEGORIES.values()))

        expected_polished = {
            "GoogleCloudPlatform": "Google Cloud Platform (GCP)",
            "ChromeDevTools": "Chrome DevTools",
            "ibm_cloud": "IBM Cloud",
            "developerportals": "Developer Portals",
            "securityascode": "Security as Code",
            "dotnet": ".NET",
            "devsecops": "DevSecOps",
            "openshift": "OpenShift",
            "eu-sovereign-cloud": "EU Sovereign Cloud Overview & TCO",
            "eu-cloud-spain": "Spain Sovereign Cloud & Private DCs",
            "eu-cloud-france-germany": "France & Germany Cloud Champions",
            "eu-cloud-italy-uk-nordics": "Italy, UK, Nordics & Benelux",
            "eu-cloud-iac-maturity": "IaC Automation & Maturity vs Hyperscalers",
            "eu-cloud-workloads-stack": "Hypervisors, IaaS, K8s & Sovereign AI",
            "eu-cloud-resilience-sla": "RPO, RTO, SLAs, DRP & Replication",
        }
        for slug, expected in expected_polished.items():
            self.assertEqual(get_readable_category(slug), expected)

    def test_eu_sovereign_pillar_registered_and_rendered(self):
        from src.config import NUBENETES_CATEGORIES
        from src.fast_enrich import DIMENSIONS as FAST_DIMS, DISPLAY_NAMES
        from src.news_digest import NewsDigestEngine
        from src.eu_sovereign_blueprints import EU_SOVEREIGN_BLUEPRINTS

        eu_slugs = [
            "eu-sovereign-cloud",
            "eu-cloud-spain",
            "eu-cloud-france-germany",
            "eu-cloud-italy-uk-nordics",
            "eu-cloud-iac-maturity",
            "eu-cloud-workloads-stack",
            "eu-cloud-resilience-sla",
        ]
        dim_name = "European Sovereign Cloud & Private DCs"
        self.assertIn(dim_name, FAST_DIMS)
        self.assertIn("European Sovereign Cloud", NewsDigestEngine.DIGEST_CATEGORIES)

        with open(os.path.join(REPO_ROOT, "v2-mkdocs.yml"), "r", encoding="utf-8") as f:
            v2_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "mkdocs.yml"), "r", encoding="utf-8") as f:
            v1_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "v2-docs/api/index.json"), "r", encoding="utf-8") as f:
            api_catalog = json.load(f)

        self.assertIn(dim_name, api_catalog.get("dimensions", []))
        api_slugs = {c["slug"] for c in api_catalog.get("categories", [])}

        for slug in eu_slugs:
            fname = f"{slug}.md"
            self.assertIn(slug, NUBENETES_CATEGORIES)
            self.assertIn(slug, DISPLAY_NAMES)
            self.assertIn(slug, FAST_DIMS[dim_name])
            self.assertIn(slug, NewsDigestEngine.DIGEST_CATEGORIES["European Sovereign Cloud"])
            self.assertIn(fname, EU_SOVEREIGN_BLUEPRINTS)
            self.assertIn(fname, v2_mkdocs_txt)
            self.assertIn(fname, v1_mkdocs_txt)
            self.assertIn(slug, api_slugs)
            v2_path = os.path.join(REPO_ROOT, "v2-docs", fname)
            self.assertTrue(os.path.exists(v2_path), f"Missing generated V2 page {v2_path}")
            with open(v2_path, "r", encoding="utf-8") as f:
                v2_body = f.read()
            self.assertIn('okf_version: "0.3"', v2_body[:600])
            self.assertIn("type: curation-hub", v2_body[:600])
            self.assertIn(EU_SOVEREIGN_BLUEPRINTS[fname].splitlines()[0], v2_body)

    def test_boilerplate_and_historical_heuristics(self):
        from src.fast_enrich import is_boilerplate_summary
        from src.v2_optimizer import V2VisionEngine

        self.assertTrue(is_boilerplate_summary("Technical documentation and implementation reference for Foo (General)."))
        self.assertTrue(is_boilerplate_summary("Curated technical resource in Kubernetes."))
        self.assertTrue(is_boilerplate_summary(""))
        self.assertFalse(
            is_boilerplate_summary(
                "Cilium provides eBPF-based networking, observability, and L7 security for Kubernetes clusters with native Gateway API support."
            )
        )

        # Active CNCF Graduated or recently pushed GitHub repo must NOT be archived despite old creation year
        self.assertFalse(
            V2VisionEngine._is_historical_item(
                {"year": "2015", "cncf_status": "graduated", "gh_pushed": "2026-11-01", "tags": ["[DE FACTO STANDARD]"]}
            )
        )
        self.assertFalse(
            V2VisionEngine._is_historical_item(
                {"year": "2019", "gh_pushed": "2025-09-12", "tags": ["[ENTERPRISE-STABLE]"]}
            )
        )
        # Pre-2022 blog post or explicitly [LEGACY] or unmaintained repo MUST be historical
        self.assertTrue(V2VisionEngine._is_historical_item({"year": "2020", "tags": ["[GUIDE]"]}))
        self.assertTrue(V2VisionEngine._is_historical_item({"year": "2025", "tags": ["[LEGACY]"]}))
        self.assertTrue(V2VisionEngine._is_historical_item({"year": "2020", "gh_pushed": "2020-05-01", "tags": []}))

    def test_okf_endpoints_and_frontmatter_present(self):
        llms_full = os.path.join(REPO_ROOT, "v2-docs/llms-full.txt")
        api_index = os.path.join(REPO_ROOT, "v2-docs/api/index.json")
        self.assertTrue(os.path.exists(llms_full), "v2-docs/llms-full.txt must exist")
        self.assertTrue(os.path.exists(api_index), "v2-docs/api/index.json must exist")
        with open(api_index, "r", encoding="utf-8") as f:
            catalog = json.load(f)
        self.assertEqual(catalog.get("okf_version"), "0.3")
        self.assertGreater(len(catalog.get("categories", [])), 50)
        for hub in ("v2-docs/ocp5.md", "v2-docs/ai-rag-okf.md"):
            with open(os.path.join(REPO_ROOT, hub), "r", encoding="utf-8") as f:
                head = f.read(600)
            self.assertIn('okf_version: "0.3"', head)
            self.assertIn("type: curation-hub", head)
            self.assertIn("trust: verified", head)

    def test_v1_bullet_regex_captures_description_without_swallowing_nested_bullets(self):
        sample = (
            "- **(2026)** [Parent Resource](https://example.com/parent) 🌟 - Full parent description here.\n"
            "  - [Nested Child](https://example.com/child) - Child description.\n"
            "- [Multiline Item](https://example.com/multi) - First line\n"
            "  continued description on indented line.\n"
        )
        pat = r'^\s*-\s*(?:\*\*\(\d{4}\)\*\*\s+)?\[([^\]]+)\]\(([^\)]+)\)([^\n]*(?:\n\s{2,}(?!\s*[-*]\s).*)*)'
        matches = list(re.finditer(pat, sample, re.MULTILINE))
        self.assertEqual(len(matches), 3)
        self.assertEqual(matches[0].group(1), "Parent Resource")
        self.assertIn("Full parent description here.", matches[0].group(3))
        self.assertEqual(matches[1].group(1), "Nested Child")
        self.assertIn("Child description.", matches[1].group(3))
        self.assertEqual(matches[2].group(1), "Multiline Item")
        self.assertIn("continued description on indented line.", matches[2].group(3))


if __name__ == "__main__":
    unittest.main()
