import argparse

def create_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure random secret keys for backends."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=32,
        help="Length of the key in characters (default: 32)"
    )
    parser.add_argument(
        "-t", "--type",
        choices=["hex", "base64", "alphanumeric"],
        default="hex",
        help="Key format type (default: hex)"
    )
    parser.add_argument(
        "-p", "--prefix",
        type=str,
        default="",
        help="Prefix to prepend to the key (e.g. 'sk_prod_')"
    )
    parser.add_argument(
        "-e", "--env",
        type=str,
        help="Format output as a .env entry using the provided variable name"
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Number of keys to generate (default: 1)"
    )
    return parser
