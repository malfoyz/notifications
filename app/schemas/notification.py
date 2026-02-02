__all__ = ("NotificationSchema", "NotificationInSchema")

from datetime import datetime

from pydantic import BaseModel

from app.constants import NotificationTypeEnum
from .user import UserSchema


class NotificationSchema(BaseModel):
    id: int
    type: NotificationTypeEnum
    text: str
    created_at: datetime
    user: UserSchema

    model_config = {
        "from_attributes": True
    }


class NotificationInSchema(BaseModel):
    type: NotificationTypeEnum
    text: str

