from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SlotCreate(BaseModel):
    activity_id: str
    start_date_time: datetime
    end_date_time: datetime
    price: Optional[int]
    max_users: Optional[int]
