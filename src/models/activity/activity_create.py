from typing import Optional

from pydantic import BaseModel, Field


class ActivityCreate(BaseModel):
    name: str
    description: Optional[str]
    x: int
    y: int
    is_private: bool = Field(default=False)
    is_active: bool = Field(default=True)
