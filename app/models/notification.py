__all__ = ("Notification",)
from tortoise import fields, models

from app.constants import NotificationTypeEnum


class Notification(models.Model):
    id = fields.IntField(primary_key=True)
    user = fields.ForeignKeyField(
        "models.User",
        related_name="notifications",
        on_delete=fields.CASCADE,
        db_index=True,
    )
    type = fields.CharEnumField(NotificationTypeEnum)
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "notifications"
