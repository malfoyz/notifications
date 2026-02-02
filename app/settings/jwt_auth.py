__all__ = (
    "JWT_SECRET_KEY",
    "JWT_ALGORITHM",
    "ACCESS_TOKEN_LIFETIME",
    "REFRESH_TOKEN_LIFETIME",
)

from decouple import config

from app.constants import TimesSecondsEnum

JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", default="HS256")
JWT_ALGORITHM: str = config("JWT_ALGORITHM")
ACCESS_TOKEN_LIFETIME = TimesSecondsEnum.FIVE_MINUTES
REFRESH_TOKEN_LIFETIME = TimesSecondsEnum.ONE_DAY * 2