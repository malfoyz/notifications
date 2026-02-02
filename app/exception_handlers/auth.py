__all__ = ("user_already_exists_handler", "invalid_credentials_handler")
from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.exceptions import UserAlreadyExistsError, InvalidCredentialsError


async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )


async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )
