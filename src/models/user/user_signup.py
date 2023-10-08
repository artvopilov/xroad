from typing import Literal, Optional

from pydantic import BaseModel


class UserSignup(BaseModel):
    username: str
    password: str
    user_type: Literal['person', 'business']

    # common
    name: str
    phone: str
    email: Optional[str]

    # person
    middle_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    city: Optional[str]

    # business
    description: Optional[str]
    address: Optional[str]
