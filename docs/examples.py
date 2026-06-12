import os
import sys

# Ensure modules in the parent directory can be imported when executing this script directly.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from formatters import apply_prefix, format_dotenv
from generators import (
    generate_alphanumeric_key,
    generate_base64_key,
    generate_hex_key,
)

def run_examples() -> None:
    """Demonstrate how to use key generation and formatting modules programmatically."""
    # 1. Generating a standard Hex key (e.g., for Flask/Django SECRET_KEY)
    django_secret = generate_hex_key(64)
    print(f"1. Django SECRET_KEY (Hex, 64 chars):\n   {django_secret}\n")

    # 2. Generating a prefixed API key (Base64 URL-safe, 48 chars key + prefix)
    raw_api_key = generate_base64_key(48)
    stripe_style_key = apply_prefix(raw_api_key, "sk_live_")
    print(f"2. Prefixed API Token:\n   {stripe_style_key}\n")

    # 3. Generating an alphanumeric database password formatted for .env file
    db_password = generate_alphanumeric_key(24)
    env_format = format_dotenv("DATABASE_PASSWORD", db_password)
    print(f"3. Environment Variable Format:\n   {env_format}\n")

if __name__ == "__main__":
    run_examples()
