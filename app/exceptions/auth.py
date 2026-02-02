__all__ = (
    "AuthenticationError",
    "InvalidCredentialsError",
    "UserAlreadyExistsError",
)


class AuthenticationError(Exception): ...


class InvalidCredentialsError(AuthenticationError):
    def __init__(self, msg: str = "Invalid credentials.") -> None:
        super().__init__(msg)


class UserAlreadyExistsError(Exception):
    def __init__(self, msg: str = "User with this username already exists.") -> None:
        super().__init__(msg)

