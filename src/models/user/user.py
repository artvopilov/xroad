from typing import Optional, List, Literal

from pydantic import BaseModel, ConfigDict, Field

from src.models.pydantic_object_id import PydanticObjectId


class User(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')

    username: str
    password: str
    user_type: Literal['person', 'business']
    phone: str
    email: Optional[str]
    image_url: Optional[str]

    # person
    person_first_name: Optional[str]
    person_middle_name: Optional[str]
    person_last_name: Optional[str]
    person_date_of_birth: Optional[str]
    person_gender: Optional[str]
    person_is_pro: Optional[bool]

    # business
    business_registration_id: Optional[str]
    business_name: Optional[str]
    business_description: Optional[str]
    business_address: Optional[str]
    business_certificate_urls: Optional[List[str]]
    business_is_verified: Optional[bool]
