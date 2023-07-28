from typing import Optional

from pydantic import BaseModel


class BusinessCreate(BaseModel):
    username: str
    password: str
    name: str
    description: Optional[str]
    phone: str
    email: Optional[str]
    address: str
