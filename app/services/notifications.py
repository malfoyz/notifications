__all__ = ("create_notification", "get_user_notifications", "delete_user_notification")

from app.constants import NotificationTypeEnum
from app.exceptions import NotificationNotFoundError
from app.models import Notification, User
from app.settings import logger


async def create_notification(
    user: User,
    type_: NotificationTypeEnum,
    text: str,
) -> Notification:
    logger.debug("Creating notification for user_id=%s, type=%s", user.id, type_)
    notification = await Notification.create(
        user=user,
        type=type_,
        text=text,
    )
    logger.info("Notification created: id=%s for user_id=%s", notification.id, user.id)
    return notification


async def get_user_notifications(
    user_id: int,
    limit: int,
    offset: int,
) -> list[Notification]:
    return await (
        Notification
        .filter(user_id=user_id)
        .select_related("user")
        .order_by("-created_at")
        .offset(offset)
        .limit(limit)
        .all()
    )


async def delete_user_notification(
    notification_id: int,
    user_id: int,
) -> None:
    deleted_count = await Notification.filter(id=notification_id, user_id=user_id).delete()
    if not deleted_count:
        logger.warning("Failed to delete notification: id=%s not found for user_id=%s", notification_id, user_id)
        raise NotificationNotFoundError()
    logger.info("Notification deleted: id=%s for user_id=%s", notification_id, user_id)



