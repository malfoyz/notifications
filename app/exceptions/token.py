__all__ = (
    "InvalidTokenError",
    "TokenError",
)


class TokenError(Exception): ...


class InvalidTokenError(TokenError):
    def __init__(self, msg: str = "Invalid token.") -> None:
        super().__init__(msg)