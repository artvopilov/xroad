from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class Service(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    business_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    name: str
    description: str
    x: int
    y: int
    is_private: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)

    # class Config:
    #     allow_population_by_field_name = True
    #     json_encoders = {ObjectId: str}
