from pydantic import BaseModel
from datetime import date


class BasePwd(BaseModel):
    value: str
    attempt_r: int
    data: date


class Pwd(BasePwd):
    id: int

    class Config:
        orm_mode = True  # can access to element with . and not only []


class BaseUser(BaseModel):
    name: str
    last_name: str
    email: str
    pwds: list[Pwd] = []

class CreateUser(BaseUser):
    ...
class User(BaseUser):
    id: int

    class Config:
        orm_mode = True  # can access to element with . and not only []
