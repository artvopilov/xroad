from typing import Optional

from .user import User


class Person(User):
    first_name: str
    middle_name: Optional[str]
    last_name: Optional[str]
    age: int
    gender: str
    city: str
    is_pro: bool = False
