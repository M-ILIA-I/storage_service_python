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
    batch_id: int
    product_id: int
    part: int
    price: float
    quantity: float
    uniq_code: UUID | None
    ean: str
    type_product: str
    product_name: str
    product_producer: str
    product_country: str
    

class ResponseDataStorageSchema(BaseModel):
    status: str
    code: int
    data: List[DataStorageSchema]
    
    
class MarksDataRequestSchema(BaseModel):
    batch_id: int
    uniq_code: UUID
    

class MarksData(BaseModel):
    UKZ: str | None = "-"
    SI: str | None = "-"
    is_sold: bool | None = False
    

class ResponseMarksSchema(BaseModel):
    status: str
    code: int
    data: MarksData
    
    