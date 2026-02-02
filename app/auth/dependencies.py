__all__ = ("get_current_user",)
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.models import User
from app.settings import JWT_SECRET_KEY, JWT_ALGORITHM, logger

security = HTTPBearer()


# TODO: декомпозировать get_current_user

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    token = credentials.credentials
    logger.debug("Authenticating user with token: %s", token[:8] + "...")
    try:
        payload = jwt.decode(
            token=token,
            key=JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
        )
        user_id = int(payload.get("sub"))
        logger.debug("Token decoded successfully: user_id=%s", user_id)
    except (JWTError, TypeError, ValueError):
        logger.warning("Invalid authentication token: %s", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    user = await User.get_or_none(id=user_id)
    if not user:
        logger.warning("User not found for user_id=%s", user_id)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    logger.info("User authenticated successfully: user_id=%s, username=%s", user.id, user.username)
    return user
