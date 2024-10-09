from pydantic import BaseModel
from uuid import UUID
from typing import List


class ProductsNameSchema(BaseModel):
    id: int
    name: str
    
    class Config():
        from_attributes = True
    
    
class ProductsProducerSchema(BaseModel):
    id: int
    name: str
    
    class Config():
        from_attributes = True
    
    
class ProductsCountrySchema(BaseModel):
    id: int
    name: str

    class Config():
        from_attributes = True

class ProductsSchema(BaseModel):
    id: int 
    nomenclature_id: int
    ean: str
    type_product: str
    
    class Config():
        from_attributes = True


class MarkSchema(BaseModel):
    id: int 
    batch_id: int
    uniq_code: UUID | None
    value: str
    type_mark: str
    is_sold: bool
    
    class Config():
        from_attributes = True
    

class BatchSchema(BaseModel):
    id: int
    product_id: int
    part: int
    price: float
    quantity: float
    
    class Config():
        from_attributes = True
        

class DataStorageSchema(BaseModel):
    product_id: int
    part: int
    price: float
    quantity: float
    uniq_code: UUID | None
    value: str
    type_mark: str
    is_sold: bool
    ean: str
    type_product: str
    product_name: str
    product_producer: str
    product_country: str
    

class ResponseDataStorageSchema(BaseModel):
    status: str
    code: int
    data: List[DataStorageSchema]
    