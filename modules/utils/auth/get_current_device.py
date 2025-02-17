import os
from fastapi import HTTPException, Depends, status
from modules.utils.auth.auth_error import AuthorizationException
from jose import JWTError, jwt
from typing import Annotated
from modules.utils.auth.get_current_token import get_current_token
from dotenv import load_dotenv
from pydantic import BaseModel
from modules.models.auth_models.device import Device
from modules.connection_to_db.database import async_session
import httpx 


class DeviceSchema(BaseModel):
    id: int
    firm_id: int
    username: str
    info: str

load_dotenv()


async def get_current_device(authorization_token: Annotated[str, Depends(get_current_token)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if authorization_token is None:
        raise AuthorizationException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    try:
        payload = jwt.decode(authorization_token, os.getenv("SECRET_KEY"), algorithms=[os.getenv('ALGORITHM')])
        
        device_id: str = payload.get("id")
        
        if device_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/getDeviceById/{device_id}")
        response.raise_for_status()  # Проверка на ошибки
        data = response.json() 
        device = data["device"]
        
    if data["status"] != "ok":
        raise credentials_exception
    return DeviceSchema(**device)
