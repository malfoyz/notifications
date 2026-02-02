__all__ = ("NotificationError", "NotificationNotFoundError")


class NotificationError(Exception): ...


class NotificationNotFoundError(NotificationError):
    def __init__(self, msg: str = "Notification not found.") -> None:
        super().__init__(msg)