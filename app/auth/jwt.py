__all__ = ("create_token", "create_access_token", "create_refresh_token")
from datetime import UTC, datetime, timedelta
from jose import jwt

from app.settings import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME, logger
from app.settings.jwt_auth import JWT_SECRET_KEY, JWT_ALGORITHM


def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    to_encode["exp"] = datetime.now(UTC) + expires_delta
    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    logger.debug("Token created for user_id=%s, expires_in=%s seconds", data.get("sub"), expires_delta.total_seconds())
    return token


def create_access_token(user_id: int) -> str:
    return create_token(
        {"sub": str(user_id)},
        timedelta(seconds=ACCESS_TOKEN_LIFETIME)
    )


def create_refresh_token(user_id: int) -> str:
    return create_token(
        {"sub": str(user_id)},
        timedelta(seconds=REFRESH_TOKEN_LIFETIME)
    )