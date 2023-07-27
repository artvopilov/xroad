from typing import Optional, List

from pydantic import BaseModel


class Business(BaseModel):
    username: str
    password: str
    name: str
    description: Optional[str]
    logo_url: Optional[str]
    phone: str
    email: Optional[str]
    address: str
    document_urls: Optional[List[str]]
    certificate_urls: Optional[List[str]]
