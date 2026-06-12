import unittest

from formatters import apply_prefix, format_dotenv

class TestFormatters(unittest.TestCase):
    """Test cases for checking key formatting and prefix logic."""

    def test_apply_prefix_with_value(self) -> None:
        key = "random_key_value"
        prefix = "sk_live_"
        self.assertEqual(apply_prefix(key, prefix), "sk_live_random_key_value")

    def test_apply_prefix_empty(self) -> None:
        key = "random_key_value"
        self.assertEqual(apply_prefix(key, ""), "random_key_value")
        self.assertEqual(apply_prefix(key, None), "random_key_value")

    def test_format_dotenv(self) -> None:
        key = "secret_value_123"
        self.assertEqual(format_dotenv("jwt_secret", key), "JWT_SECRET=secret_value_123")
        self.assertEqual(format_dotenv("  api_key  ", key), "API_KEY=secret_value_123")

if __name__ == "__main__":
    unittest.main()
