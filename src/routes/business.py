from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth_utils import AuthUtils
from src.models import Business as BusinessModel
from src.route_deps import RouteDeps
from src.schemas import Business as BusinessSchema

router = APIRouter(prefix='/business')


@router.post('/signup')
async def signup(business_model: BusinessModel):
    business_schema = BusinessSchema.objects(username=str(business_model.username))
    if business_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Business with this username already exists')
    business_info = business_model.dict()
    business_info['password'] = AuthUtils.compute_password_hash(business_info['password'])
    new_business_schema = BusinessSchema(**business_info).save()
    return {'username': new_business_schema.username}


@router.post('/signin')
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    business_schema = BusinessSchema.objects(username=form_data.username).first()
    if not business_schema or not AuthUtils.verify_password(form_data.password, business_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(business_schema.username)
    return {'access_token': access_token, 'token_type': "bearer"}


@router.get('/me', response_model=BusinessModel)
async def me(current_business: Annotated[BusinessModel, Depends(RouteDeps.get_current_business)]):
    return current_business
