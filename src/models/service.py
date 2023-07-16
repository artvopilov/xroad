from typing import Dict, Any

from pydantic import BaseModel


class Service(BaseModel):
    name: str
    description: str
    x: int
    y: int
    is_private: bool
    is_active: bool
