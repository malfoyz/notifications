from fastapi import status

from ..utils import random_username


_LOGIN_PATH = "/auth/login"


async def test_login(client, user):
    response = await client.post(_LOGIN_PATH, json={"username": user["username"]})
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "access" in data
    assert "refresh" in data


async def test_login_non_existent_user(client):
    response = await client.post(_LOGIN_PATH, json={"username": random_username()})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
