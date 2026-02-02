import random

from fastapi import status

from app.constants import NotificationTypeEnum

_DEFAULT_AVATAR_URL = "https://example.com/avatar.png"
_NOTIFICATIONS_PATH = "/notifications"
_LOGIN_PATH = "/auth/login"
_REGISTER_PATH = "/auth/register"


async def _create_notification(client, headers, text="Test notification", notification_type=None):
    payload = {
        "type": notification_type or random.choice([type.value for type in NotificationTypeEnum]),
        "text": text,
    }
    response = await client.post(_NOTIFICATIONS_PATH, json=payload, headers=headers)
    return response.json()


async def test_create_notification(client, user):
    payload = {
        "type": random.choice([type.value for type in NotificationTypeEnum]),
        "text": "Test notification",
    }
    response = await client.post(_NOTIFICATIONS_PATH, json=payload, headers=user["headers"])
    assert response.status_code == status.HTTP_201_CREATED

    notification = response.json()
    assert notification["text"] == payload["text"]
    assert notification["type"] == payload["type"]


async def test_get_notifications(client, user):
    created_notification = await _create_notification(client, user["headers"])

    response = await client.get(_NOTIFICATIONS_PATH, headers=user["headers"])
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert any(notify["id"] == created_notification["id"] for notify in data)


async def test_delete_existing_notification(client, user):
    created_notification = await _create_notification(client, user["headers"])

    response = await client.delete(f"{_NOTIFICATIONS_PATH}/{created_notification["id"]}", headers=user["headers"])
    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_delete_non_existent_notification(client, user):
    response = await client.delete(f"{_NOTIFICATIONS_PATH}/{random.randint(1, 10000)}", headers=user["headers"])
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_notifications_pagination(client, user):
    for i in range(5):
        await _create_notification(client, user["headers"], text="Test notification {i}")

    # GET с limit=2, offset=0
    response = await client.get(f"{_NOTIFICATIONS_PATH}?limit=2&offset=0", headers=user["headers"])
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 2
    for notif in data:
        assert notif["user"]["username"] == user["username"]
        assert "avatar_url" in notif["user"]

    # GET с limit=2, offset=2
    response = await client.get(f"{_NOTIFICATIONS_PATH}?limit=2&offset=2", headers=user["headers"])
    data_offset = response.json()
    assert len(data_offset) == 2
    for notif in data_offset:
        assert notif["user"]["username"] == user["username"]
        assert "avatar_url" in notif["user"]

    # GET с limit=10, offset=0 → вернет все 5 уведомлений
    response = await client.get(f"{_NOTIFICATIONS_PATH}?limit=10&offset=0", headers=user["headers"])
    data_all = response.json()
    assert len(data_all) == 5
