import sys
from typing import Callable

from cli import create_parser
from formatters import apply_prefix, format_dotenv
from generators import (
    generate_alphanumeric_key,
    generate_base64_key,
    generate_hex_key,
)

def get_generator_function(key_type: str) -> Callable[[int], str]:
    """Map the key type string to its corresponding generator function."""
    generators = {
        "hex": generate_hex_key,
        "base64": generate_base64_key,
        "alphanumeric": generate_alphanumeric_key,
    }
    return generators[key_type]

def process_key(generator_func: Callable[[int], str], length: int, prefix: str, env_name: str | None) -> str:
    """Generate, prefix, and format a single key."""
    raw_key = generator_func(length)
    prefixed_key = apply_prefix(raw_key, prefix)
    if env_name:
        return format_dotenv(env_name, prefixed_key)
    return prefixed_key

def main() -> None:
    """Orchestrate argument parsing and key generation/formatting."""
    parser = create_parser()
    args = parser.parse_args()

    try:
        generator_func = get_generator_function(args.type)
        for _ in range(args.count):
            result = process_key(generator_func, args.length, args.prefix, args.env)
            print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
