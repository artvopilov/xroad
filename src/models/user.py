from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    name: str
    age: int
    type: str
