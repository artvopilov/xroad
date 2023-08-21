from typing import Optional

from .user_create import UserCreate


class PersonCreate(UserCreate):
    first_name: str
    middle_name: Optional[str]
    last_name: Optional[str]
    age: int
    gender: str
    city: str
    is_pro: Optional[bool]
