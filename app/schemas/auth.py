__all__ = ("RegisterRequestSchema", "RefreshTokenSchema", "LoginRequestSchema", "TokenResponseSchema")
from pydantic import BaseModel


class RegisterRequestSchema(BaseModel):
    username: str


class LoginRequestSchema(BaseModel):
    username: str


class TokenResponseSchema(BaseModel):
    access: str
    refresh: str


class RefreshTokenSchema(BaseModel):
    refresh: str
