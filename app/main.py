__all__ = ("app",)
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.exception_handlers import invalid_credentials_handler, invalid_token_handler, notification_not_found_handler
from app.exception_handlers.auth import user_already_exists_handler
from app.exceptions import UserAlreadyExistsError, InvalidCredentialsError, InvalidTokenError, NotificationNotFoundError
from app.routers.auth import router as auth_router
from app.routers.notifications import router as notifications_router
from app.settings import DATABASE_URL

app = FastAPI(title="Notification Service")


_exception_handlers = {
    UserAlreadyExistsError: user_already_exists_handler,
    InvalidCredentialsError: invalid_credentials_handler,
    InvalidTokenError: invalid_token_handler,
    NotificationNotFoundError: notification_not_found_handler,
}
_routers = (
    auth_router,
    notifications_router,
)

for error, handler in _exception_handlers.items():
    app.add_exception_handler(error, handler)

for router in _routers:
    app.include_router(router)


@app.get("/ping", tags=["Health Check"])
async def ping():
    return "pong"


register_tortoise(
    app=app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models.user", "app.models.notification"]},
    generate_schemas=True,
    add_exception_handlers=True,
)