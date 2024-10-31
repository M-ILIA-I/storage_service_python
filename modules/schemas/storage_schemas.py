from pydantic import BaseModel
from uuid import UUID
from typing import List
from datetime import datetime


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
    device_id: int
    product_id: int
    price: float
    quantity: float
    dt_send: datetime
    dt_update: datetime
    dt_create: datetime
    
    class Config():
        from_attributes = True
        

class DataStorageSchema(BaseModel):
    batch_id: int
    product_id: int
    device_id: int
    device_name: str = ""
    price: float
    quantity: float
    dt_send: datetime
    dt_update: datetime
    dt_create: datetime
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
    uniq_code: UUID | None
    

class MarksData(BaseModel):
    product_name: str = ""
    batch_id: int = 0
    device_name: str = ""
    UKZ: str | None = "-"
    SI: str | None = "-"
    dt_update: datetime = ""
    is_sold: bool | None = False
    

class ResponseMarksSchema(BaseModel):
    status: str
    code: int
    data: MarksData
    
    
class RequestEditMarksDataSchema(BaseModel):
    batch_id: int
    UKZ: str | None
    SI: str | None
        

class ResponseEditMarksSchema(BaseModel):
    status: str
    code: int
    data: int
    