from typing import Optional

from pydantic import BaseModel


class ActivityUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    x: Optional[float]
    y: Optional[float]
    is_private: Optional[bool]
    is_active: Optional[bool]
