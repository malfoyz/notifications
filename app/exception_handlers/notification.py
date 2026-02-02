__all__ = ("notification_not_found_handler",)
from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.exceptions import NotificationNotFoundError


async def notification_not_found_handler(request: Request, exc: NotificationNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)}
    )
