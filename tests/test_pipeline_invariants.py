import os
import re
import unittest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestPipelineInvariants(unittest.TestCase):
    """Guardrails enforcing zero-token publishing, Mandate 11 sync, category consistency, and parser safety."""

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

    def test_new_hubs_registered_consistently_across_pipeline(self):
        from src.config import NUBENETES_CATEGORIES
        from src.fast_enrich import DIMENSIONS as FAST_DIMS, get_readable_category
        from src.news_digest import NewsDigestEngine

        for slug, expected_title in [("ocp5", "OCP 5"), ("ai-rag-okf", "AI RAG OKF")]:
            self.assertIn(slug, NUBENETES_CATEGORIES)
            self.assertEqual(get_readable_category(slug), expected_title)
            self.assertTrue(any(slug in cats for cats in FAST_DIMS.values()))
            self.assertTrue(any(slug in cats for cats in NewsDigestEngine.DIGEST_CATEGORIES.values()))

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
