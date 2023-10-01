from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str


# def validate_password_complexity(password: str):
#     if (
#             len(password < 8)
#             or not any(char.isupper() for char in password)
#             or not any(char in "!@#$%^&*()" for char in password)):
#         raise ValueError(
#             "Password must be at least 8 characters long and contain one uppercase letter and have one special symbol")
#     return password
