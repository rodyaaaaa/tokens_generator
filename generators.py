import math
import secrets
import string

def generate_hex_key(length: int) -> str:
    """Generate a secure random hexadecimal key of the specified length."""
    num_bytes = math.ceil(length / 2)
    return secrets.token_hex(num_bytes)[:length]

def generate_base64_key(length: int) -> str:
    """Generate a secure random URL-safe base64 key of the specified length."""
    num_bytes = math.ceil(length * 3 / 4)
    # Generate slightly more bytes to ensure we meet the requested length.
    extra_bytes = num_bytes + 2
    return secrets.token_urlsafe(extra_bytes)[:length]

def generate_alphanumeric_key(length: int) -> str:
    """Generate a secure random alphanumeric key of the specified length."""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
