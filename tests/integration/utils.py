__all__ = ("random_username",)
import uuid


def random_username() -> str:
    return f"new_user_{uuid.uuid4().hex[:8]}"
