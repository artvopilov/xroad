from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class User(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    username: str
    first_name: str
    middle_name: Optional[str]
    last_name: Optional[str]
    image_url: Optional[str]
    phone: str
    email: Optional[str]
    age: int
    gender_id: int
    city_id: int
    is_pro: bool = False
