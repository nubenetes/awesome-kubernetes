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
            "eu-cloud-germany": "Germany Sovereign Cloud & Private DCs",
            "eu-cloud-france": "France Sovereign Cloud & Private DCs",
            "eu-cloud-italy": "Italy Sovereign Cloud & Private DCs",
            "eu-cloud-benelux": "Netherlands & Benelux Cloud & DCs",
            "eu-cloud-switzerland-dach": "Switzerland & Austria (Alpine Sovereign)",
            "eu-cloud-nordics": "Nordics Green Cloud & AI Factories",
            "eu-cloud-uk": "United Kingdom Sovereign Cloud & DCs",
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
            "eu-cloud-germany",
            "eu-cloud-france",
            "eu-cloud-italy",
            "eu-cloud-benelux",
            "eu-cloud-switzerland-dach",
            "eu-cloud-nordics",
            "eu-cloud-uk",
            "eu-cloud-iac-maturity",
            "eu-cloud-workloads-stack",
            "eu-cloud-resilience-sla",
        ]
        retired_slugs = ["eu-cloud-france-germany", "eu-cloud-italy-uk-nordics"]
        dim_name = "European Sovereign Cloud & Private DCs"
        self.assertIn(dim_name, FAST_DIMS)
        self.assertIn("European Sovereign Cloud", NewsDigestEngine.DIGEST_CATEGORIES)

        with open(os.path.join(REPO_ROOT, "v2-mkdocs.yml"), "r", encoding="utf-8") as f:
            v2_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "mkdocs.yml"), "r", encoding="utf-8") as f:
            v1_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "docs/overrides/main.html"), "r", encoding="utf-8") as f:
            overrides_txt = f.read()
        with open(os.path.join(REPO_ROOT, "v2-docs/api/index.json"), "r", encoding="utf-8") as f:
            api_catalog = json.load(f)

        self.assertIn(dim_name, api_catalog.get("dimensions", []))
        api_slugs = {c["slug"] for c in api_catalog.get("categories", [])}

        for rslug in retired_slugs:
            rfname = f"{rslug}.md"
            self.assertNotIn(rslug, NUBENETES_CATEGORIES)
            self.assertNotIn(rfname, EU_SOVEREIGN_BLUEPRINTS)
            self.assertFalse(os.path.exists(os.path.join(REPO_ROOT, "docs", rfname)))
            self.assertFalse(os.path.exists(os.path.join(REPO_ROOT, "v2-docs", rfname)))
            self.assertRegex(v2_mkdocs_txt, rf"{re.escape(rfname)}:\s+eu-cloud-")

        for slug in eu_slugs:
            fname = f"{slug}.md"
            self.assertIn(slug, NUBENETES_CATEGORIES)
            self.assertIn(slug, DISPLAY_NAMES)
            self.assertIn(slug, FAST_DIMS[dim_name])
            self.assertIn(slug, NewsDigestEngine.DIGEST_CATEGORIES["European Sovereign Cloud"])
            self.assertIn(fname, EU_SOVEREIGN_BLUEPRINTS)
            self.assertIn(fname, v2_mkdocs_txt)
            self.assertIn(fname, v1_mkdocs_txt)
            self.assertIn(f"/{slug}/", overrides_txt)
            self.assertIn(slug, api_slugs)
            v2_path = os.path.join(REPO_ROOT, "v2-docs", fname)
            self.assertTrue(os.path.exists(v2_path), f"Missing generated V2 page {v2_path}")
            with open(v2_path, "r", encoding="utf-8") as f:
                v2_body = f.read()
            self.assertIn('okf_version: "0.3"', v2_body[:600])
            self.assertIn("type: curation-hub", v2_body[:600])
            self.assertIn(EU_SOVEREIGN_BLUEPRINTS[fname].splitlines()[0], v2_body)

        with open(os.path.join(REPO_ROOT, "v2-docs/eu-sovereign-cloud.md"), "r", encoding="utf-8") as f:
            eu_overview_txt = f.read()
        self.assertIn('<div class="eu-hub-grid"', eu_overview_txt)
        for card_slug in eu_slugs[1:]:
            self.assertIn(f'href="/{card_slug}/"', eu_overview_txt)
        self.assertLess(
            eu_overview_txt.index("### European Country and Regional Pre-Sales Hubs"),
            eu_overview_txt.index("### The 4 Levels of Cloud Sovereignty"),
        )

    def test_neoclouds_pillar_registered_and_rendered(self):
        from src.config import NUBENETES_CATEGORIES
        from src.fast_enrich import DIMENSIONS as FAST_DIMS, DISPLAY_NAMES
        from src.news_digest import NewsDigestEngine
        from src.neoclouds_blueprints import NEOCLOUDS_BLUEPRINTS

        neocloud_slugs = [
            "neoclouds",
            "neoclouds-europe",
            "neoclouds-north-america",
            "neoclouds-apac",
            "neoclouds-mena",
            "neoclouds-latam-africa",
            "neoclouds-architecture-stack",
            "neoclouds-iac-finops-sla",
        ]
        dim_name = "Neoclouds & GPU AI Clouds"
        self.assertIn(dim_name, FAST_DIMS)
        self.assertIn(dim_name, NewsDigestEngine.DIGEST_CATEGORIES)

        with open(os.path.join(REPO_ROOT, "v2-mkdocs.yml"), "r", encoding="utf-8") as f:
            v2_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "mkdocs.yml"), "r", encoding="utf-8") as f:
            v1_mkdocs_txt = f.read()
        with open(os.path.join(REPO_ROOT, "docs/overrides/main.html"), "r", encoding="utf-8") as f:
            overrides_txt = f.read()
        with open(os.path.join(REPO_ROOT, "v2-docs/api/index.json"), "r", encoding="utf-8") as f:
            api_catalog = json.load(f)

        self.assertIn(dim_name, api_catalog.get("dimensions", []))
        api_slugs = {c["slug"] for c in api_catalog.get("categories", [])}

        for slug in neocloud_slugs:
            fname = f"{slug}.md"
            self.assertIn(slug, NUBENETES_CATEGORIES)
            self.assertIn(slug, DISPLAY_NAMES)
            self.assertIn(slug, FAST_DIMS[dim_name])
            self.assertIn(slug, NewsDigestEngine.DIGEST_CATEGORIES[dim_name])
            self.assertIn(fname, NEOCLOUDS_BLUEPRINTS)
            self.assertIn(fname, v2_mkdocs_txt)
            self.assertIn(fname, v1_mkdocs_txt)
            self.assertIn(f"/{slug}/", overrides_txt)
            self.assertIn(slug, api_slugs)
            v2_path = os.path.join(REPO_ROOT, "v2-docs", fname)
            self.assertTrue(os.path.exists(v2_path), f"Missing generated V2 page {v2_path}")
            with open(v2_path, "r", encoding="utf-8") as f:
                v2_body = f.read()
            self.assertIn('okf_version: "0.3"', v2_body[:600])
            self.assertIn("type: curation-hub", v2_body[:600])
            self.assertIn(NEOCLOUDS_BLUEPRINTS[fname].splitlines()[0], v2_body)

        with open(os.path.join(REPO_ROOT, "v2-docs/neoclouds.md"), "r", encoding="utf-8") as f:
            neo_overview_txt = f.read()
        self.assertIn('<div class="eu-hub-grid"', neo_overview_txt)
        for card_slug in neocloud_slugs[1:] + ["eu-sovereign-cloud"]:
            self.assertIn(f'href="/{card_slug}/"', neo_overview_txt)
        self.assertIn("### Neoclouds vs Sovereign Cloud: Overlap, Convergence and Legal Distinction", neo_overview_txt)
        self.assertIn("CLOUD Act", neo_overview_txt)

        with open(os.path.join(REPO_ROOT, "v2-docs/neoclouds-europe.md"), "r", encoding="utf-8") as f:
            neo_eu_txt = f.read()
        for eu_sister in (
            "eu-cloud-benelux",
            "eu-cloud-france",
            "eu-cloud-germany",
            "eu-cloud-spain",
            "eu-cloud-italy",
            "eu-cloud-nordics",
            "eu-cloud-switzerland-dach",
            "eu-cloud-uk",
        ):
            self.assertIn(f"/{eu_sister}/", neo_eu_txt)

    def test_neoclouds_blueprints_have_clickable_provider_links_and_valid_anchors(self):
        from markdown.extensions.toc import slugify
        from src.neoclouds_blueprints import NEOCLOUDS_BLUEPRINTS

        min_links = {
            "neoclouds.md": 25,
            "neoclouds-europe.md": 25,
        }
        for fname, body in NEOCLOUDS_BLUEPRINTS.items():
            ext_links = re.findall(r"\]\((https://[^)\s]+)\)", body)
            expected_min = min_links.get(fname, 6)
            self.assertGreaterEqual(
                len(ext_links),
                expected_min,
                f"Expected >= {expected_min} clickable external provider/tool links in {fname}, got {len(ext_links)}",
            )

            headings = re.findall(r"^#{1,6}\s+(.+)$", body, re.MULTILINE)
            heading_slugs = {slugify(h.strip(), "-") for h in headings}
            internal_anchors = re.findall(r'(?:href="#|\(#)([^")]+)', body)
            self.assertGreater(len(internal_anchors), 0, f"Expected internal TOC/card anchors in {fname}")
            for anchor in internal_anchors:
                self.assertIn(
                    anchor,
                    heading_slugs,
                    f"Broken internal anchor #{anchor} in {fname}; known slugs={sorted(heading_slugs)}",
                )

            v2_path = os.path.join(REPO_ROOT, "v2-docs", fname)
            with open(v2_path, "r", encoding="utf-8") as f:
                v2_body = f.read()
            for url in ext_links[:10]:
                self.assertIn(url, v2_body, f"Rendered V2 page {fname} missing blueprint link {url}")

        with open(os.path.join(REPO_ROOT, "docs/static/v2_elite.css"), "r", encoding="utf-8") as f:
            css_txt = f.read()
        self.assertGreaterEqual(
            css_txt.count("--md-typeset-a-color"),
            2,
            "v2_elite.css must set --md-typeset-a-color for both light and slate dark mode",
        )

    def test_announce_banner_preserves_permanent_flagships(self):
        with open(os.path.join(REPO_ROOT, "docs/overrides/main.html"), "r", encoding="utf-8") as f:
            html_txt = f.read()
        m = re.search(r"\{%\s*block announce\s*%\}(.*?)\{%\s*endblock\s*%\}", html_txt, re.DOTALL)
        self.assertIsNotNone(m, "announce block must exist in docs/overrides/main.html")
        banner = m.group(1)
        for href in (
            "/eu-sovereign-cloud/",
            "/neoclouds/",
            "/ocp5/",
            "/ai-rag-okf/",
            "/tech-digest/",
            "/videos/",
        ):
            self.assertIn(href, banner, f"Permanent link {href} missing from announce banner")
        self.assertNotIn("/eu-cloud-spain/", banner)

    def test_v2_mermaid_blocks_have_bounded_line_lengths(self):
        for rel in (
            "v2-docs/eu-sovereign-cloud.md",
            "v2-docs/introduction.md",
            "v2-docs/neoclouds.md",
            "v2-docs/neoclouds-architecture-stack.md",
        ):
            with open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8") as f:
                txt = f.read()
            blocks = re.findall(r"```mermaid\n(.*?)\n```", txt, re.DOTALL)
            self.assertGreaterEqual(len(blocks), 1, f"Expected Mermaid diagram in {rel}")
            for block in blocks:
                body = re.sub(r"%%\{.*?\}%%", "", block, flags=re.DOTALL)
                for label in re.findall(r'(?:\"([^\"]+)\"|[\[{]\(?([^\]}\n]+)\)?)', body):
                    raw = label[0] or label[1]
                    for part in re.split(r"<br\s*/?>", raw):
                        clean = part.strip().strip('"')
                        self.assertLessEqual(
                            len(clean),
                            32,
                            f"Mermaid line too long ({len(clean)} chars) in {rel}: {clean!r}",
                        )
            if rel == "v2-docs/eu-sovereign-cloud.md":
                for hub_label in (
                    "Germany Sovereign",
                    "France Sovereign",
                    "Netherlands & Benelux",
                    "Switzerland & Austria",
                    "Spain Sovereign",
                    "Italy Sovereign",
                    "Nordics 3-AZ & Green",
                    "United Kingdom",
                ):
                    self.assertIn(hub_label, blocks[0])

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

    def test_quicknav_popovers_have_css_anchor_pairings(self):
        with open(os.path.join(REPO_ROOT, "docs/overrides/main.html"), "r", encoding="utf-8") as f:
            html_txt = f.read()
        with open(os.path.join(REPO_ROOT, "docs/static/v2_elite.css"), "r", encoding="utf-8") as f:
            css_txt = f.read()

        targets = sorted(set(re.findall(r'popovertarget="(nb-pop-[^"]+)"', html_txt)))
        self.assertGreater(len(targets), 10)
        for pop_id in targets:
            self.assertIn(f'[popovertarget="{pop_id}"]', css_txt, f"Missing anchor-name CSS for {pop_id}")
            self.assertIn(f"#{pop_id}", css_txt, f"Missing position-anchor CSS for #{pop_id}")

    def test_pr_gatekeeper_two_stage_security_and_doc_invariants(self):
        from src.safety_readme import check_readme

        linter_path = os.path.join(REPO_ROOT, ".github/workflows/07.2.markdown_linter.yml")
        guardian_path = os.path.join(REPO_ROOT, ".github/workflows/07.1.pr_guardian.yml")
        pub_path = os.path.join(REPO_ROOT, ".github/workflows/04.1.agentic_v2_publish.yml")
        deploy_path = os.path.join(REPO_ROOT, ".github/workflows/06.deploy_final.yml")

        with open(linter_path, "r", encoding="utf-8") as f:
            linter_txt = f.read()
            linter_yaml = yaml.safe_load(linter_txt)
        self.assertEqual(linter_yaml.get("permissions"), {"contents": "read"})
        self.assertNotIn("GEMINI_API_KEY", linter_txt, "Stage 1 sandbox must hold 0 AI secrets")
        self.assertNotIn("pr_guardian", linter_txt, "Stage 1 sandbox must not execute PR Python scripts")

        with open(guardian_path, "r", encoding="utf-8") as f:
            guardian_txt = f.read()
            guardian_yaml = yaml.safe_load(guardian_txt)
        triggers = guardian_yaml.get(True, guardian_yaml.get("on", {}))
        self.assertIn("workflow_run", triggers)
        self.assertNotIn("pull_request_target", triggers, "Must use workflow_run rather than pull_request_target")
        self.assertNotIn("pull_request.head.ref", guardian_txt, "Stage 2 must NEVER check out untrusted PR code")
        self.assertIn("ref: master", guardian_txt)
        self.assertEqual(guardian_yaml.get("permissions", {}).get("models"), "read")

        for downstream_path in (pub_path, deploy_path):
            with open(downstream_path, "r", encoding="utf-8") as f:
                wf = yaml.safe_load(f)
            wf_triggers = wf.get(True, wf.get("on", {}))
            upstream_list = wf_triggers.get("workflow_run", {}).get("workflows", [])
            self.assertIn("07.1. PR Guardian AI", upstream_list)

        for doc_name in ("AGENTS.md", "GEMINI.md", "CLAUDE.md", "README.md"):
            self.assertTrue(os.path.exists(os.path.join(REPO_ROOT, doc_name)), f"Missing {doc_name}")
        self.assertTrue(check_readme(), "README.md failed 15-section integrity check")


if __name__ == "__main__":
    unittest.main()
