from typing import Optional

from .user_create import UserCreate


class BusinessCreate(UserCreate):
    name: str
    description: Optional[str]
    address: str
