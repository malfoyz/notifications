__all__ = ("invalid_token_handler",)
from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.exceptions import InvalidTokenError


async def invalid_token_handler(request: Request, exc: InvalidTokenError):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": str(exc)}
    )
