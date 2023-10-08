from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SlotUpdate(BaseModel):
    activity_id: str
    start_date_time: Optional[datetime]
    end_date_time: Optional[datetime]
    price: Optional[int]
    max_users: Optional[int]
