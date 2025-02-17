from fastapi import Depends, HTTPException
from modules.connection_to_db.database import get_async_session, get_async_session_auth
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from modules.schemas.storage_schemas import ResponseDataStorageSchema, DataStorageSchema
from modules.models.batch import Batch
from modules.models.product import Product
from modules.models.products_country import ProductsCountry
from modules.models.products_name import ProductsName
from modules.models.products_group import ProductsGroup
from modules.models.products_producer import ProductsProducer
from modules.models.mark import Mark
from modules.schemas.storage_schemas import MarksDataRequestSchema, ResponseMarksSchema, MarksData, RequestEditMarksDataSchema, ResponseEditMarksSchema
from modules.models.auth_models.device import Device


class StorageHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session), session_auth: AsyncSession = Depends(get_async_session_auth)):
        self.session = session
        self.session_auth = session_auth
        
    
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
                    Batch.id.label("batch_id"),
                    Product.id.label("product_id"),
                    Batch.store_id,
                    Batch.price,
                    Batch.quantity,
                    Batch.dt_send,
                    Batch.dt_update,
                    Batch.dt_create,
                    subquery.c.uniq_code.label("uniq_code"),
                    Product.ean,
                    ProductsGroup.name.label("group_name"),
                    Product.type_product,
                    ProductsName.name.label("product_name"),
                    ProductsProducer.name.label("product_producer"),
                    ProductsCountry.name.label("product_country")
                )
                .select_from(Batch)
                .outerjoin(subquery, subquery.c.batch_id == Batch.id)  # Условие INNER JOIN
                .join(Product)
                .outerjoin(ProductsGroup)
                .outerjoin(ProductsCountry)
                .outerjoin(ProductsName)
                .outerjoin(ProductsProducer)
            )
            result = await self.session.execute(query)
            data = result.mappings().fetchall()
            
            data_storage = [DataStorageSchema.model_validate(i) for i in data]
            
            return ResponseDataStorageSchema(data=data_storage, status="ok", code=200)
                
        except HTTPException as e:
            return self.Error(str(e))
        
        
    async def get_marks_data(self, request_data: MarksDataRequestSchema) -> ResponseMarksSchema:
        try:          
            query = (select(Mark, ProductsName.name, Batch.device_id, Batch.dt_update, Batch.id)
                    .select_from(Mark)
                    .join(Batch)
                    .join(Product)
                    .join(ProductsName)
                    .where(Mark.batch_id == request_data.batch_id))
                                
            result = await self.session.execute(query)
            response = MarksData()
            marks = result.fetchall()
            
            if marks:
                for item, name, device_id, dt_update, batch_id in marks:
                    device = await self.session_auth.get(Device, device_id)
                    if item.type_mark.value == 1:
                        response.UKZ = item.value
                    else:
                        response.SI = item.value
                    response.is_sold = item.is_sold
                    response.device_name = device.name
                    response.product_name = name
                    response.dt_update = dt_update.strftime("%Y-%m-%d %H:%M")
                    response.batch_id = batch_id
            
                return ResponseMarksSchema(code=200, status="ok", data=response)
            else:
                batch = await self.session.get(Batch, request_data.batch_id)
                device = await self.session_auth.get(Device, batch.device_id)
                response.device_name = device.name
                return ResponseMarksSchema(code=200, status="ok", data=response)
            
        except HTTPException as e:
            return self.Error(str(e))
            
            
    async def edit_marks(self, request_data: RequestEditMarksDataSchema) -> ResponseEditMarksSchema:
        try:
            query = select(Mark).where(Mark.batch_id == request_data.batch_id)
            result = await self.session.execute(query)
            marks = result.fetchall()
            
            for mark in marks:
                if mark[0].type_mark.name == "UKZ":
                    mark[0].value = request_data.UKZ
                    request_data.UKZ = "-"
                else:
                    mark[0].value = request_data.SI
                    request_data.SI = "-"
                    
            await self.session.commit()
            return ResponseEditMarksSchema(status="ok", code=200, data=request_data.batch_id)
        except HTTPException as e:
            return self.Error(str(e))
            