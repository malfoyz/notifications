__all__ = ("UserSchema",)
from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    avatar_url: str

    model_config = {
        "from_attributes": True
    }