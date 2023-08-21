from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth_utils import AuthUtils
from src.models import UserCreate as UserCreateModel, User as UserModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/signup', response_model=UserModel)
async def user_signup(user_create_model: UserCreateModel):
    user_schema = UserSchema.objects(username=str(user_create_model.username))
    if user_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this username already exists')
    user_create_info = user_create_model.dict()
    user_create_info['password'] = AuthUtils.compute_password_hash(user_create_info['password'])
    user_schema = UserSchema(**user_create_info).save()
    return user_schema.to_mongo()


@router.post('/signin')
async def user_signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_schema = UserSchema.objects(username=form_data.username).first()
    if not user_schema or not AuthUtils.verify_password(form_data.password, user_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(user_schema.username)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('', response_model=UserModel)
async def user(user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]):
    return user_schema.to_mongo()
