def apply_prefix(key: str, prefix: str) -> str:
    """Prepends a prefix to the generated key."""
    if not prefix:
        return key
    return f"{prefix}{key}"

def format_dotenv(variable_name: str, key: str) -> str:
    """Format the key as an environment variable assignment."""
    clean_name = variable_name.strip().upper()
    return f"{clean_name}={key}"
