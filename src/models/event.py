from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    name: str
    x: int
    y: int
    start: datetime
    end: datetime
