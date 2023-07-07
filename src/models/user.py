from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: Optional[str]
    username: str
    password: str
    image_url: Optional[str]
    phone: str
    email: Optional[str]
    age: int
    gender_id: int
    city_id: int
    is_pro: bool = False
