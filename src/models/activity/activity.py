from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from src.models.pydantic_object_id import PydanticObjectId


class Activity(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    user_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    name: str
    description: Optional[str]
    x: float
    y: float
    is_private: bool
    is_active: bool
