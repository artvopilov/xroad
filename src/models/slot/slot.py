from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from src.models.pydantic_object_id import PydanticObjectId


class Slot(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    activity_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    start_date_time: datetime
    end_date_time: datetime
    price: Optional[int]
    max_users: Optional[int]
