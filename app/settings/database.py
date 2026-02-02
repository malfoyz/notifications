__all__ = ("DATABASE_URL",)

from decouple import config


DATABASE_URL = config("DATABASE_URL")
