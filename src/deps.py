from datetime import datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.auth_utils import AuthUtils
from src.models import User as UserModel
from src.schemas import User as UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='user/signin')


async def get_current_user(access_token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = AuthUtils.extract_access_token_payload(access_token)
        username = payload.get('username')
        expire = payload.get('exp')
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Missing username')
        if datetime.fromtimestamp(expire) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token expired')
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials')
    user_schema = UserSchema.objects(username=username).first()
    if not user_schema:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username')
    print(user_schema)
    user_info = user_schema.to_json()
    print(user_info)
    user_info.pop('password')
    return UserModel(**user_info)
