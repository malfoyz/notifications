from fastapi import status

from app.models import User
from ..utils import random_username


_DEFAULT_AVATAR_URL = "https://example.com/avatar.png"
_REGISTER_PATH = "/auth/register"


async def test_register_new_username(client):
    response = await client.post(_REGISTER_PATH, json={"username": random_username()})
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "access" in data
    assert "refresh" in data


async def test_register_same_username(client):
    username = random_username()
    await User.create(username=username, avatar_url=_DEFAULT_AVATAR_URL)

    response = await client.post(_REGISTER_PATH, json={"username": username})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert data['detail'] == "User with this username already exists."
