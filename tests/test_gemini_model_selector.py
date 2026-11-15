import asyncio
import os
import unittest
from unittest.mock import patch

import src.gemini_utils as gemini_utils
from src.gemini_utils import (
    classify_model_metadata,
    discover_optimal_models,
    is_flash_model,
    is_pro_frontier_model,
    select_models_for_task,
)


def _build_catalog(raw_entries):
    meta_map = {}
    pool = []
    for raw in raw_entries:
        meta = classify_model_metadata(raw)
        meta_map[meta["name"]] = meta
        pool.append(meta["name"])
    return pool, meta_map


class TestGeminiModelSelector(unittest.TestCase):
    def test_gen4_hydrogen_beats_3_8_flash_for_fast_tasks(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-3.8-flash", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-3.7-flash", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-4-carbon", "inputTokenLimit": 1048576, "outputTokenLimit": 32768},
            {"name": "models/gemini-4-argon", "inputTokenLimit": 1048576, "outputTokenLimit": 32768},
            {"name": "models/gemini-4-hydrogen", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-omni-1.2-flash", "inputTokenLimit": 131072, "outputTokenLimit": 65536},
            {"name": "models/gemini-flash-latest", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
        ])
        fast = select_models_for_task(pool, meta, prefer_flash=True, use_grounding=False)
        self.assertEqual(fast[0], "gemini-4-hydrogen")
        self.assertEqual(fast[1], "gemini-3.8-flash")
        self.assertNotIn("gemini-4-carbon", fast)
        self.assertNotIn("gemini-4-argon", fast)
        # Omni and evergreen fall behind main versioned models
        self.assertGreater(fast.index("gemini-flash-latest"), fast.index("gemini-3.7-flash"))
        self.assertGreater(fast.index("gemini-omni-1.2-flash"), fast.index("gemini-flash-latest"))

    def test_unknown_future_codename_scheme_auto_adopted(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-4-hydrogen", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-4-carbon", "inputTokenLimit": 1048576, "outputTokenLimit": 32768},
            # Brand-new Gen-5 naming without any legacy keywords or descriptive prose
            {"name": "models/gemini-5-zephyr", "description": "Gemini 5 Zephyr", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-5-titan", "description": "Gemini 5 Titan", "inputTokenLimit": 2097152, "outputTokenLimit": 32768},
        ])
        fast = select_models_for_task(pool, meta, prefer_flash=True, use_grounding=False)
        frontier = select_models_for_task(pool, meta, prefer_flash=False, use_grounding=True)

        # Gen 5 outranks Gen 4 on both paths without hardcoding "zephyr"/"titan"
        self.assertEqual(fast[0], "gemini-5-zephyr")
        self.assertIn("gemini-4-hydrogen", fast)
        self.assertEqual(frontier[0], "gemini-5-titan")
        self.assertIn("gemini-4-carbon", frontier)

    def test_description_fallback_infers_tiers_for_new_names(self):
        pool, meta = _build_catalog([
            {
                "name": "models/gemini-5-aurora",
                "description": "Most capable complex reasoning flagship model.",
                "inputTokenLimit": 1048576,
                "outputTokenLimit": 65536,
            },
            {
                "name": "models/gemini-5-breeze",
                "description": "Fast everyday workhorse model for rapid responses.",
                "inputTokenLimit": 1048576,
                "outputTokenLimit": 65536,
            },
        ])
        self.assertEqual(meta["gemini-5-aurora"]["tier"], "frontier")
        self.assertEqual(meta["gemini-5-breeze"]["tier"], "fast")

        fast = select_models_for_task(pool, meta, prefer_flash=True)
        frontier = select_models_for_task(pool, meta, prefer_flash=False)
        self.assertEqual(fast, ["gemini-5-breeze"])
        self.assertEqual(frontier, ["gemini-5-aurora"])

    def test_minor_version_and_stability_ordering(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-3.8-flash", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-3.10-flash-preview", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-3.10-flash-exp", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
            {"name": "models/gemini-3.10-flash", "inputTokenLimit": 1048576, "outputTokenLimit": 65536},
        ])
        fast = select_models_for_task(pool, meta, prefer_flash=True)
        self.assertEqual(
            fast,
            [
                "gemini-3.10-flash",
                "gemini-3.10-flash-preview",
                "gemini-3.10-flash-exp",
                "gemini-3.8-flash",
            ],
        )

    def test_env_overrides_take_priority(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-4-hydrogen"},
            {"name": "models/gemini-4-carbon"},
        ])
        with patch.dict(os.environ, {"GEMINI_FAST_MODEL": "gemini-custom-fast", "GEMINI_PRO_MODEL": "gemini-custom-pro"}):
            fast = select_models_for_task(pool, meta, prefer_flash=True)
            frontier = select_models_for_task(pool, meta, use_grounding=True)
        self.assertEqual(fast[0], "gemini-custom-fast")
        self.assertEqual(frontier[0], "gemini-custom-pro")

    def test_role_predicates(self):
        self.assertTrue(is_flash_model("gemini-4-hydrogen"))
        self.assertTrue(is_flash_model("gemini-3.8-flash"))
        self.assertTrue(is_pro_frontier_model("gemini-4-carbon"))
        self.assertTrue(is_pro_frontier_model("gemini-4-argon"))
        self.assertFalse(is_pro_frontier_model("gemini-3-flash-preview"))

    def test_speed_tokens_outrank_frontier_tokens_in_compound_names(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-4-ultra"},
            {"name": "models/gemini-4-ultra-fast"},
            {"name": "models/gemini-4-ultra-lite"},
        ])
        self.assertEqual(meta["gemini-4-ultra"]["tier"], "frontier")
        self.assertEqual(meta["gemini-4-ultra-fast"]["tier"], "fast")
        self.assertEqual(meta["gemini-4-ultra-lite"]["tier"], "lite")
        self.assertEqual(select_models_for_task(pool, meta, prefer_flash=True)[0], "gemini-4-ultra-fast")

    def test_unversioned_aliases_and_grounding_override(self):
        pool, meta = _build_catalog([
            {"name": "models/gemini-pro"},
            {"name": "models/gemini-pro-latest"},
            {"name": "models/gemini-4-carbon"},
            {"name": "models/gemini-4-hydrogen"},
        ])
        self.assertTrue(meta["gemini-pro"]["is_evergreen"])
        self.assertTrue(meta["gemini-pro-latest"]["is_evergreen"])
        # use_grounding=True must force frontier path even when prefer_flash=True
        grounding = select_models_for_task(pool, meta, prefer_flash=True, use_grounding=True)
        self.assertEqual(grounding[0], "gemini-4-carbon")
        self.assertNotIn("gemini-4-hydrogen", grounding)

    def test_discovery_fallback_is_not_sticky(self):
        class _FakeResp:
            def __init__(self, code, payload):
                self.status_code = code
                self._payload = payload

            def json(self):
                return self._payload

        responses = [
            _FakeResp(500, {}),
            _FakeResp(200, {
                "models": [
                    {
                        "name": "models/gemini-5-photon",
                        "supportedGenerationMethods": ["generateContent"],
                        "inputTokenLimit": 1048576,
                        "outputTokenLimit": 65536,
                    }
                ]
            }),
        ]

        class _FakeClient:
            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                return False

            async def get(self, *args, **kwargs):
                return responses.pop(0)

        with patch.object(gemini_utils, "DISCOVERED_MODELS", []), \
             patch.object(gemini_utils, "DISCOVERED_MODEL_METADATA", {}), \
             patch.object(gemini_utils, "_DISCOVERY_USED_FALLBACK", False), \
             patch.object(gemini_utils, "GEMINI_API_KEYS", ["k1"]), \
             patch("src.gemini_utils.httpx.AsyncClient", return_value=_FakeClient()):
            first = asyncio.run(discover_optimal_models())
            self.assertIn("gemini-4-hydrogen", first)
            second = asyncio.run(discover_optimal_models())
            self.assertEqual(second, ["gemini-5-photon"])


if __name__ == "__main__":
    unittest.main()
