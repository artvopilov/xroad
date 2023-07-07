from typing import Optional, List

from pydantic import BaseModel


class Business(BaseModel):
    name: str
    address: str
    document_urls: Optional[List[str]]
    username: str
    password: str
    image_url: Optional[str]
    phone: str
    email: Optional[str]
    description: Optional[str]
    certificate_urls: Optional[List[str]]
