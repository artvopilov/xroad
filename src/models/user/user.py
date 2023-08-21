from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class User(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    username: str
    user_type: str
    phone: str
    email: Optional[str]
