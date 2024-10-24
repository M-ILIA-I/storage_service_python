from fastapi import Depends, HTTPException
from modules.connection_to_db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from modules.schemas.storage_schemas import ResponseDataStorageSchema, DataStorageSchema
from modules.models.batch import Batch
from modules.models.product import Product
from modules.models.products_country import ProductsCountry
from modules.models.products_name import ProductsName
from modules.models.products_producer import ProductsProducer
from modules.models.mark import Mark
from modules.schemas.storage_schemas import MarksDataRequestSchema, ResponseMarksSchema, MarksData


class StotageHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        
    
    def Error(message: str):
        return HTTPException(status_code=400, detail=message)
    
    
    async def get_storage_data(self) -> ResponseDataStorageSchema:
        try:
            # Подзапрос для получения batch_id и uniq_code
            subquery = (
                select(Mark.batch_id, Mark.uniq_code)
                .group_by(Mark.batch_id, Mark.uniq_code)
            ).subquery()

            # Основной запрос с INNER JOIN
            query = (
                select(
                    Product.id.label("product_id"),
                    Batch.id.label("batch_id"),
                    Batch.device_id,
                    Batch.price,
                    Batch.quantity,
                    Batch.dt_send,
                    Batch.dt_update,
                    Batch.dt_create,
                    subquery.c.uniq_code.label("uniq_code"),
                    Product.ean,
                    Product.type_product,
                    ProductsName.name.label("product_name"),
                    ProductsProducer.name.label("product_producer"),
                    ProductsCountry.name.label("product_country")
                )
                .select_from(Batch)
                .join(subquery, subquery.c.batch_id == Batch.id)  # Условие INNER JOIN
                .join(Product)
                .join(ProductsCountry)
                .join(ProductsName)
                .join(ProductsProducer)
            )
            result = await self.session.execute(query)
            data = result.mappings().all()

            data_storage = [DataStorageSchema(**i) for i in data]
            
            return ResponseDataStorageSchema(data=data_storage, status="ok", code=200)
                
        except HTTPException as e:
            return self.Error(str(e))
        
        
    async def get_marks_data(self, request_data: MarksDataRequestSchema) -> ResponseMarksSchema:
        try:
            query = select(Mark).where(
                                        and_(
                                        Mark.batch_id == request_data.batch_id,
                                        Mark.uniq_code == request_data.uniq_code
                                        ))
            result = await self.session.execute(query)
            response = MarksData()
            
            for item in result.scalars().all():
                if item.type_mark.value == 1:
                    response.UKZ = item.value
                else:
                    response.SI = item.value
                response.is_sold = item.is_sold
            
            return ResponseMarksSchema(code=200, status="ok", data=response)
        except HTTPException as e:
            return self.Error(str(e))
            