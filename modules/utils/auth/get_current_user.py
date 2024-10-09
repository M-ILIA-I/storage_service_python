import os
from fastapi import HTTPException, Depends, status
from modules.utils.auth.auth_error import AuthorizationException
from jose import JWTError, jwt
from typing import Annotated
from modules.utils.auth.get_current_token import get_current_token
from dotenv import load_dotenv
from pydantic import BaseModel
from modules.connection_to_db.database import async_session
import httpx


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
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(f"http://localhost:8000/getUserById/{user_id}")
    #     response.raise_for_status()  # Проверка на ошибки
    #     data = response.json() 
    #     user = data["user"]
    
    # if data["status"] != "ok":
    #     raise credentials_exception
    # return CurrentUser(**user)
    return CurrentUser(id=1, firm_id=1, username="ilya", sold=1, permissions="admin")
