from typing import Optional, List

from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class Business(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    username: str
    name: str
    description: Optional[str]
    logo_url: Optional[str]
    phone: str
    email: Optional[str]
    address: str
    document_urls: Optional[List[str]]
    certificate_urls: Optional[List[str]]
