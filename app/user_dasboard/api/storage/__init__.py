from fastapi import APIRouter
from .get_storage_data import router as get_storage_router


storage_api = APIRouter(tags=["storage"])

storage_api.include_router(get_storage_router)