__all__ = ("router",)
from fastapi import APIRouter

from app.schemas import TokenResponseSchema, RegisterRequestSchema, LoginRequestSchema, RefreshTokenSchema
from app.services import register_user, login_user, refresh_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=TokenResponseSchema)
async def register(data: RegisterRequestSchema):
    return await register_user(data.username)


@router.post("/login", response_model=TokenResponseSchema)
async def login(data: LoginRequestSchema):
    return await login_user(data.username)


@router.post("/refresh", response_model=TokenResponseSchema)
async def refresh_token(data: RefreshTokenSchema):
    return await refresh_access_token(data.refresh)
