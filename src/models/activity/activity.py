import datetime
from typing import Optional, Dict

from pydantic import BaseModel, ConfigDict, Field

from src.models.pydantic_object_id import PydanticObjectId


class Activity(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    user_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
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
