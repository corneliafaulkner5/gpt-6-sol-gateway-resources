import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class ResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/resources.json").read_text(encoding="utf-8"))

    def test_verified_resource_has_live_model_contract(self):
        self.assertEqual(self.data["model"], "gpt-6-sol")
        self.assertEqual(self.data["checked"], "2026-10-07")
        rows = self.data["verified_resources"]
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["status"], "verified")
        self.assertEqual(row["model_id"], "gpt-6-sol")
        self.assertEqual(row["base_url"], "https://argolink.io/v1")
        self.assertEqual(row["endpoint"], "/responses")
        self.assertEqual(row["context_tokens"], 1050000)
        self.assertEqual(row["max_output_tokens"], 128000)
        self.assertEqual(row["reasoning_efforts"], ["low", "medium", "high", "xhigh", "max"])

    def test_prices_and_long_context_are_numeric(self):
        row = self.data["verified_resources"][0]
        for price in row["pricing_usd_per_million_tokens"].values():
            self.assertIsInstance(price, (int, float))
            self.assertGreaterEqual(price, 0)
        self.assertEqual(row["long_context"]["threshold_tokens"], 272000)
        self.assertEqual(row["long_context"]["input_multiplier"], 2.0)
        self.assertEqual(row["long_context"]["output_multiplier"], 1.5)
        self.assertIsNone(row["rate_limits"])

    def test_unverified_rows_are_explicit(self):
        rows = self.data["unverified_resources"]
        self.assertGreaterEqual(len(rows), 3)
        self.assertTrue(all(row["status"] in {"not_verified", "adapter_only"} for row in rows))
        self.assertTrue(all(row.get("reason") for row in rows))


if __name__ == "__main__":
    unittest.main()
