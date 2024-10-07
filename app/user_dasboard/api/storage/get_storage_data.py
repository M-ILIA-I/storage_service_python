from ..dependencies import *
from fastapi import APIRouter
from modules.schemas.storage_schemas import ResponseDataStorageSchema
from app.user_dasboard.handlers.storage.storage_handler import StotageHandler


router = APIRouter()


@router.get("/getStorageData", responses={200:{"model": ResponseDataStorageSchema}})
async def get_storage_data(handler: Annotated[StotageHandler, Depends(StotageHandler)]):
    return await handler.get_storage_data()