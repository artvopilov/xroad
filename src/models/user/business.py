from typing import Optional, List

from .user import User


class Business(User):
    name: str
    description: Optional[str]
    address: str
    document_urls: Optional[List[str]]
    certificate_urls: Optional[List[str]]
