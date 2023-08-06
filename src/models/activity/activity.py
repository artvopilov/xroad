from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class Activity(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    business_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    name: str
    description: str
    x: int
    y: int
    is_private: bool = False
    is_active: bool = True
