from ..dependencies import *
from modules.schemas.storage_schemas import ResponseEditMarksSchema, RequestEditMarksDataSchema
from app.user_dasboard.handlers.storage.storage_handler import StorageHandler
from modules.utils.auth.get_current_user import get_current_user


router = APIRouter()


@router.post("/editMarks", responses={200:{"model": ResponseEditMarksSchema}})
async def edit_marks(
    handler: Annotated[StorageHandler, Depends(StorageHandler)],
    request_data: RequestEditMarksDataSchema,
    # user = Depends(get_current_user)
):
    return await handler.edit_marks(request_data)