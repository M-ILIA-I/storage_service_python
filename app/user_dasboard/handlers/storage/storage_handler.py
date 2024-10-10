from fastapi import Depends, HTTPException
from modules.connection_to_db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from modules.schemas.storage_schemas import ResponseDataStorageSchema, DataStorageSchema
from modules.models.batch import Batch
from modules.models.product import Product
from modules.models.products_country import ProductsCountry
from modules.models.products_name import ProductsName
from modules.models.products_producer import ProductsProducer
from modules.models.nomenclature import Nomenclature
from modules.models.mark import Mark


class StotageHandler():
    
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        
    
    def Error(message: str):
        return HTTPException(status_code=400, detail=message)
    
    
    async def get_storage_data(self) -> ResponseDataStorageSchema:
        try:
            query = (
                select(
                        Product.id.label("product_id"), 
                        Batch.part,
                        Batch.price,
                        Batch.quantity,
                        Mark.uniq_code,
                        Mark.value,
                        Mark.type_mark,
                        Mark.is_sold,
                        Product.ean,
                        Product.type_product,
                        ProductsCountry.name.label("product_country"),
                        ProductsName.name.label("product_name"),
                        ProductsProducer.name.label("product_producer")
                )
                .join(Mark)
                .join(Product)  # JOIN с таблицей Product
                .join(Nomenclature)
                .join(ProductsCountry)  # JOIN с таблицей ProductsCountry
                .join(ProductsName)  # JOIN с таблицей ProductsName
                .join(ProductsProducer)
            )
            result = await self.session.execute(query)
            data = result.mappings().all()
            
            data_storage = [DataStorageSchema(**i) for i in data]
            
            return ResponseDataStorageSchema(data=data_storage, status="ok", code=200)
                
        except HTTPException as e:
            return self.Error(str(e))