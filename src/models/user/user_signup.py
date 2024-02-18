from typing import Literal, Optional

from pydantic import BaseModel


class UserSignup(BaseModel):
    username: str
    password: str
    user_type: Literal['person', 'business']
    phone: str
    email: Optional[str]
