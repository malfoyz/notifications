__all__ = ("User",)
from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=64, unique=True)
    avatar_url = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    notifications: fields.ReverseRelation["Notification"]

    class Meta:
        table = "users"
