from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    middle_name: Optional[str]
    last_name: Optional[str]
    age: int
    gender_id: int
    city_id: int
    phone: str
    email: Optional[str]
    is_pro: Optional[bool]
