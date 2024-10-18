from fastapi import APIRouter
from .get_series_by_batch_id import router as get_series_by_batch_id_router

series_api_router = APIRouter(tags=["Series"])

series_api_router.include_router(get_series_by_batch_id_router)