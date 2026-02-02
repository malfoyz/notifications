__all__ = ("user",)
import pytest

from .utils import random_username

_DEFAULT_AVATAR_URL = "https://example.com/avatar.png"


@pytest.fixture
async def user(client):
    username = random_username()
    response = await client.post("/auth/register", json={"username": username})
    tokens = response.json()
    yield {
        "username": username,
        "access": tokens["access"],
        "refresh": tokens["refresh"],
        "headers": {"Authorization": f"Bearer {tokens['access']}"}
    }