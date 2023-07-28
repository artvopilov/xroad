from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field
from datetime import datetime

from src.models.pydantic_object_id import PydanticObjectId


class ServiceSlot(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    service_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    start_date_time: datetime
    end_date_time: datetime
    price: Optional[int]
    max_users: Optional[int]
