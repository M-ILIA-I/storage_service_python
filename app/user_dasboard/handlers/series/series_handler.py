from modules.connection_to_db.database import get_async_session, get_async_session_auth
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from sqlalchemy.future import select
from modules.models.series import Series
from modules.models.document import Document
from modules.models.partner import Partner
from modules.schemas.series_schemas import SeriesSchema, GetSeriesResponseSchema
from modules.models.product import Product
from modules.models.batch import Batch
from modules.models.products_name import ProductsName
from modules.models.products_country import ProductsCountry
from modules.models.products_producer import ProductsProducer
from modules.models.products_group import ProductsGroup
from modules.models.auth_models.device import Device


class SeriesHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session), session_auth: AsyncSession = Depends(get_async_session_auth)):
        self.session = session
        self.session_auth = session_auth
        
    
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
                    Partner.name_short.label("partner_short_name"),
                    ProductsCountry.name.label("product_country"),
                    ProductsName.name.label("product_name"),
                    ProductsProducer.name.label("product_producer"),
                    ProductsGroup.name.label("product_group"),
                    Product.ean.label("ean")
                )
                .select_from(Series)
                .join(Batch)
                .join(Product)
                .join(Document)
                .outerjoin(Partner)
                .outerjoin(ProductsName)
                .outerjoin(ProductsCountry)
                .outerjoin(ProductsProducer)
                .outerjoin(ProductsGroup)
                .where(Series.batch_id == batch_id)
            )
            result = await self.session.execute(query)
            result = result.mappings().fetchall()
            print(result)
            data = []
            
            for item in result:
                device = await self.session_auth.get(Device, item["device_id"])
                serie = SeriesSchema().model_validate(item)
                serie.device_name = device.name
                data.append(serie)
                
            return GetSeriesResponseSchema(status="ok", code=200, data=data)
        
        except HTTPException as e:
            return self.Error(str(e))