import string
import unittest

from generators import (
    generate_alphanumeric_key,
    generate_base64_key,
    generate_hex_key,
)

class TestGenerators(unittest.TestCase):
    """Test cases for checking cryptographic key generation logic."""

    def test_hex_key_length(self) -> None:
        for length in [8, 16, 32, 63, 64]:
            key = generate_hex_key(length)
            self.assertEqual(len(key), length)

    def test_hex_key_charset(self) -> None:
        key = generate_hex_key(128)
        hex_chars = string.hexdigits.lower()
        self.assertTrue(all(c in hex_chars for c in key.lower()))

    def test_base64_key_length(self) -> None:
        for length in [8, 16, 32, 45, 64]:
            key = generate_base64_key(length)
            self.assertEqual(len(key), length)

    def test_base64_key_urlsafe(self) -> None:
        key = generate_base64_key(256)
        allowed = string.ascii_letters + string.digits + "-_"
        self.assertTrue(all(c in allowed for c in key))

    def test_alphanumeric_key_length(self) -> None:
        for length in [8, 16, 32, 50]:
            key = generate_alphanumeric_key(length)
            self.assertEqual(len(key), length)

    def test_alphanumeric_key_charset(self) -> None:
        key = generate_alphanumeric_key(256)
        allowed = string.ascii_letters + string.digits
        self.assertTrue(all(c in allowed for c in key))

if __name__ == "__main__":
    unittest.main()
