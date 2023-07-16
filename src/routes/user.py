from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth_utils import AuthUtils
from src.models import User as UserModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema

router = APIRouter(prefix='/user')


@router.post('/signup')
async def signup(user_model: UserModel):
    user_schema = UserSchema.objects(username=str(user_model.username))
    if user_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this username already exists')
    user_info = user_model.dict()
    user_info['password'] = AuthUtils.compute_password_hash(user_info['password'])
    schema = UserSchema(**user_info).save()
    return {'username': schema.username}


@router.post('/signin')
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_schema = UserSchema.objects(username=form_data.username).first()
    if not user_schema or not AuthUtils.verify_password(form_data.password, user_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(user_schema.username)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/me', response_model=UserModel)
async def me(current_user: Annotated[UserModel, Depends(RouteDeps.get_current_user)]):
    return current_user
