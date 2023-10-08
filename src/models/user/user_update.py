from typing import Optional, List

from pydantic import BaseModel


class UserUpdate(BaseModel):
    # common
    name: Optional[str]
    phone: Optional[str]
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
