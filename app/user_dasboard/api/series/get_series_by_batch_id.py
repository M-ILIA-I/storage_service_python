from ..dependencies import *
from modules.schemas.series_schemas import GetSeriesResponseSchema
from app.user_dasboard.handlers.series.series_handler import SeriesHandler


router = APIRouter()


@router.get("/getSeriesByBatchId/{batch_id}", responses={200:{"model" : GetSeriesResponseSchema}})
async def get_series_by_batch_id(batch_id: int, handler: Annotated[SeriesHandler, Depends(SeriesHandler)]):
    return await handler.get_series_by_batch_id(batch_id=batch_id)