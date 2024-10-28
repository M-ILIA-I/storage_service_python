from modules.connection_to_db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from sqlalchemy.future import select
from modules.models.series import Series
from modules.models.document import Document
from modules.models.partner import Partner
from modules.schemas.series_schemas import SeriesSchema, GetSeriesResponseSchema


class SeriesHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        
    
    def Error(msg: str):
        return HTTPException(detail=msg, status_code=400)
    
    
    async def get_series_by_batch_id(self, batch_id: int) -> GetSeriesResponseSchema:
        try:
            # Основной запрос с INNER JOIN
            query = (
                select(
                    Series.id,
                    Series.device_id,
                    Series.batch_id,
                    Series.document_id,
                    Series.dt_expiration,
                    Series.num_came,
                    Series.num_rest,
                    Series.price_ro,
                    Series.perc_ws,
                    Series.price_ws,
                    Series.perc_nds_in,
                    Series.perc_rozn,
                    Series.perc_nds,
                    Series.price_full,
                    Partner.name_short.label("partner_short_name")
                )
                .select_from(Series)
                .join(Document)
                .join(Partner)
                .where(Series.batch_id == batch_id)
            )
            result = await self.session.execute(query)
            data = result.fetchall()
            
            data = [
                {**{col.name: getattr(item, col.name) for col in Series.__table__.columns}, 
                'partner_short_name': item.partner_short_name}
                for item in data
            ]
            return GetSeriesResponseSchema(status="ok", code=200, data=data)
        
        except HTTPException as e:
            return self.Error(str(e))