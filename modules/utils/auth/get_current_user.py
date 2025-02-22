import os
from fastapi import HTTPException, Depends, status
from modules.utils.auth.auth_error import AuthorizationException
from jose import JWTError, jwt
from typing import Annotated
from modules.utils.auth.get_current_token import get_current_token
from dotenv import load_dotenv
from pydantic import BaseModel
from modules.models.auth_models.user import User
from modules.connection_to_db.database import async_session, async_session_auth


class CurrentUser(BaseModel):
    id: int
    firm_id: int
    username: str
    sold: int
    permissions: str
    
    
load_dotenv()


async def get_current_user(authorization_token:  Annotated[str, Depends(get_current_token)])->CurrentUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if authorization_token is None:
        raise AuthorizationException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        payload = jwt.decode(authorization_token, os.getenv("SECRET_KEY"), algorithms=[os.getenv('ALGORITHM')])
        user_id: str = payload.get("id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    async with async_session_auth() as session:
        user = await session.get(User, user_id)
        
    return CurrentUser(**user.__dict__)
