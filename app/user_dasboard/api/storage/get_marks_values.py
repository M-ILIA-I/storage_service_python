from ..dependencies import *
from fastapi import APIRouter
from modules.schemas.storage_schemas import ResponseMarksSchema, MarksDataRequestSchema
from app.user_dasboard.handlers.storage.storage_handler import StotageHandler
from modules.utils.auth.get_current_user import get_current_user


router = APIRouter()


@router.post("/getMarksData", responses={200:{"model": ResponseMarksSchema}})
async def get_storage_data(
    handler: Annotated[StotageHandler, Depends(StotageHandler)],
    request_data: MarksDataRequestSchema,
    # user = Depends(get_current_user)
):
    return await handler.get_storage_data(request_data)