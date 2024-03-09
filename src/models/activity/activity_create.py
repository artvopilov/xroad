import datetime
from typing import Optional, Dict

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    name: str
    description: Optional[str]
    conditions: Optional[str]
    schedule: Optional[Dict]
    period_start: Optional[datetime.date]
    period_end: Optional[datetime.date]
    x: float
    y: float
    is_private: Optional[bool]
    is_active: Optional[bool]
