from typing import Optional, List

from pydantic import BaseModel


class BusinessUpdate(BaseModel):
    business_name: Optional[str]
    business_description: Optional[str]