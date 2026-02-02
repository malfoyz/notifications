__all__ = ("NotificationTypeEnum",)

import enum


class NotificationTypeEnum(enum.StrEnum):
    LIKE = "like"
    COMMENT = "comment"
    REPOST = "repost"