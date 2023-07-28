from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field

from src.models.pydantic_object_id import PydanticObjectId


class ServiceSlotBooking(BaseModel):
    _config = ConfigDict(allow_population_by_field_name=True)

    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias='_id')
    slot_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    user_id: PydanticObjectId = Field(default_factory=PydanticObjectId)
    is_accepted: bool = False
    is_paid: bool = False
