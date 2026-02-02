from fastapi import status


_REFRESH_PATH = "/auth/refresh"


async def test_refresh_token(client, user):
    response = await client.post(_REFRESH_PATH, json={"refresh": user["refresh"]})
    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "refresh" in data
    assert data["refresh"] == user["refresh"]

    assert "access" in data
