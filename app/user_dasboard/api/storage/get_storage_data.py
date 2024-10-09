from ..dependencies import *
from fastapi import APIRouter
from modules.schemas.storage_schemas import ResponseDataStorageSchema
from app.user_dasboard.handlers.storage.storage_handler import StotageHandler
from modules.utils.auth.get_current_user import get_current_user

router = APIRouter()


@router.get("/getStorageData", responses={200:{"model": ResponseDataStorageSchema}})
async def get_storage_data(
    handler: Annotated[StotageHandler, Depends(StotageHandler)],
    user = Depends(get_current_user)
):
    return await handler.get_storage_data()