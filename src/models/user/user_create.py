from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    user_type: str
    phone: str
    email: Optional[str]
