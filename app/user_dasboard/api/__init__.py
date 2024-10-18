from fastapi import APIRouter
from .storage import storage_api
from .series import series_api_router


api_storage_service = APIRouter()

api_storage_service.include_router(storage_api)
api_storage_service.include_router(series_api_router)

