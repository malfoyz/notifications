__all__ = ("register_user", "login_user", "refresh_access_token")
from jose import jwt, JWTError

from app.auth.jwt import create_access_token, create_refresh_token
from app.exceptions import UserAlreadyExistsError, InvalidCredentialsError, InvalidTokenError
from app.models import User
from app.settings import JWT_SECRET_KEY, JWT_ALGORITHM, logger

HARDCODED_AVATAR = "https://example.com/avatar.png"


async def register_user(username: str) -> dict[str, int | str]:
    logger.debug("Attempting to register user: username=%s", username)

    user_exists = await User.filter(username=username).exists()
    if user_exists:
        logger.warning("Registration failed: user already exists username=%s", username)
        raise UserAlreadyExistsError()

    user = await User.create(username=username, avatar_url=HARDCODED_AVATAR)
    logger.info("User registered successfully: id=%s, username=%s", user.id, username)

    return {
        "user_id": user.id,
        "access": create_access_token(user.id),
        "refresh": create_refresh_token(user.id),
    }


async def login_user(username: str) -> dict[str, str]:
    logger.debug("Login attempt: username=%s", username)

    user = await User.get_or_none(username=username)
    if not user:
        logger.warning("Login failed: invalid credentials username=%s", username)
        raise InvalidCredentialsError()

    logger.info("Login successful: user_id=%s, username=%s", user.id, username)
    return {
        "access": create_access_token(user.id),
        "refresh": create_refresh_token(user.id),
    }


async def refresh_access_token(refresh_token: str) -> dict[str, str]:
    try:
        payload = jwt.decode(
            token=refresh_token,
            key=JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
        )
    except JWTError:
        raise InvalidTokenError()

    user_id = payload.get("sub")
    if not user_id:
        raise InvalidTokenError()

    try:
        new_access = create_access_token(int(user_id))
    except JWTError:
        raise InvalidTokenError()
    return {"access": new_access, "refresh": refresh_token}
