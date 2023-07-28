from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ServiceSlotCreate(BaseModel):
    start_date_time: datetime
    end_date_time: datetime
    price: Optional[int]
    max_users: Optional[int]
