import asyncio
import unittest
from unittest.mock import patch

from src.critical_asset_monitor import run_audit


class TestCriticalAssetMonitor(unittest.TestCase):
    def test_preserves_review_required_and_recovers_dead_entries(self):
        fake_inv = {
            "https://review.example.com": {
                "tags": ["[DE FACTO STANDARD]"],
                "status": "review_required",
                "health_score": 50.0,
            },
            "https://dead.example.com": {
                "tags": ["[ENTERPRISE-STABLE]"],
                "status": "dead",
                "health_score": 0.0,
            },
            "https://live.example.com": {
                "tags": ["[DE FACTO STANDARD]"],
                "status": "online",
                "health_score": 100.0,
            },
        }
        status_responses = {
            "https://review.example.com": 404,
            "https://dead.example.com": 200,
            "https://live.example.com": 404,
        }

        async def _fake_probe(client, global_sem, host_sems, url):
            return url, status_responses[url]

        saved_calls = []

        with patch("src.critical_asset_monitor.load_inventory", return_value=fake_inv), \
             patch("src.critical_asset_monitor._probe_url", side_effect=_fake_probe), \
             patch("src.critical_asset_monitor.save_inventory", side_effect=lambda inv: saved_calls.append(dict(inv))):
            exit_code = asyncio.run(run_audit(dry_run=False))

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(saved_calls), 1)
        self.assertEqual(fake_inv["https://review.example.com"]["status"], "review_required")
        self.assertEqual(fake_inv["https://dead.example.com"]["status"], "online")
        self.assertEqual(fake_inv["https://dead.example.com"]["health_score"], 100.0)
        self.assertEqual(fake_inv["https://live.example.com"]["status"], "offline")
        self.assertEqual(fake_inv["https://live.example.com"]["health_score"], 0.0)


if __name__ == "__main__":
    unittest.main()
