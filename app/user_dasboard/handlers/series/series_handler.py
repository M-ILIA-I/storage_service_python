from modules.connection_to_db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from sqlalchemy.future import select
from modules.models.series import Series
from modules.schemas.series_schemas import SeriesSchema, GetSeriesResponseSchema


class SeriesHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        
    
    def Error(msg: str):
        return HTTPException(detail=msg, status_code=400)
    
    
    async def get_series_by_batch_id(self, batch_id: int) -> GetSeriesResponseSchema:
        try:
            query = select(Series).where(Series.batch_id == batch_id)
            result = await self.session.execute(query)
            series = result.fetchall()
            data = [SeriesSchema(**item[0].__dict__) for item in series]
            
            return GetSeriesResponseSchema(status="ok", code=200, data=data)
        
        except HTTPException as e:
            return self.Error(str(e))