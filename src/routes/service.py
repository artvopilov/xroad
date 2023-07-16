from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Business as BusinessModel
from src.models import Service as ServiceModel
from src.route_deps import RouteDeps
from src.schemas import Service as ServiceSchema

router = APIRouter(prefix='/service')


@router.post('/create')
async def create(
    service_model: ServiceModel,
    current_business: Annotated[BusinessModel, Depends(RouteDeps.get_current_business)]
):
    service_schema = ServiceSchema.objects(name=str(service_model.name))
    if service_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Service with this name already exists')
    service_info = service_model.dict()
    new_service_schema = ServiceSchema(**service_info, business=current_business).save()
    return {'name': new_service_schema.name}
