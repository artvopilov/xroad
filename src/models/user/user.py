from typing import Optional, List, Literal

from pydantic import BaseModel, ConfigDict, Field

from src.models.pydantic_object_id import PydanticObjectId


class User(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    username: str
    password: str
    user_type: Literal['person', 'business']

    # common
    name: str
    phone: str
    email: Optional[str]
    image_url: Optional[str]

    # person
    middle_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    city: Optional[str]
    is_pro: Optional[bool]

    # business
    description: Optional[str]
    address: Optional[str]
    document_urls: Optional[List[str]]
    certificate_urls: Optional[List[str]]
