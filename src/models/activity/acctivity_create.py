from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


class ActivityCreate(BaseModel):
    name: str
    description: str
    x: int
    y: int
    is_private: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)
