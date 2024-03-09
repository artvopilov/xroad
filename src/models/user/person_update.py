from typing import Optional, List

from pydantic import BaseModel


class PersonUpdate(BaseModel):
    person_first_name: Optional[str]
    person_middle_name: Optional[str]
    person_last_name: Optional[str]
    person_date_of_birth: Optional[str]
    person_gender: Optional[str]
