__all__ = ("router",)
from fastapi import APIRouter, Depends, status

from app.auth.dependencies import get_current_user
from app.models import User
from app.schemas import NotificationInSchema, NotificationSchema
from app.services import (
    create_notification as create_notification_service,
    get_user_notifications as get_user_notifications_service,
    delete_user_notification
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "",
    response_model=NotificationSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_notification(
    data: NotificationInSchema,
    current_user: User = Depends(get_current_user),
) -> NotificationSchema:
    notification = await create_notification_service(
        user=current_user,
        type_=data.type,
        text=data.text,
    )
    return NotificationSchema.model_validate(notification)


@router.get(
    "",
    response_model=list[NotificationSchema],
)
async def get_user_notifications(
    limit: int = 20,
    offset: int = 0,
    current_user: User = Depends(get_current_user),
) -> list[NotificationSchema]:
    notifications = await get_user_notifications_service(
        user_id=current_user.id,
        limit=limit,
        offset=offset,
    )
    return [NotificationSchema.model_validate(notification) for notification in notifications]


@router.delete(
    "/{notification_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_notification(
    notification_id: int,
    current_user: User = Depends(get_current_user),
) -> None:
    await delete_user_notification(notification_id, current_user.id)