from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List
from datetime import datetime
from typing import Optional


class ProductsNameSchema(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes = True)
    
    
class ProductsProducerSchema(BaseModel):
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes = True)
    
    
class ProductsCountrySchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes = True)

class ProductsSchema(BaseModel):
    id: int 
    nomenclature_id: int
    ean: str
    type_product: str
    
    model_config = ConfigDict(from_attributes = True)


class MarkSchema(BaseModel):
    id: int 
    batch_id: int
    uniq_code: UUID | None
    value: str
    type_mark: str
    is_sold: bool
    
    model_config = ConfigDict(from_attributes = True)
    

class BatchSchema(BaseModel):
    id: int
    device_id: int
    product_id: int
    price: float
    quantity: float
    dt_send: datetime
    dt_update: datetime
    dt_create: datetime
    
    model_config = ConfigDict(from_attributes = True)
        

class DataStorageSchema(BaseModel):
    batch_id: Optional[int] = None
    product_id: Optional[int] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = ""
    price: Optional[float] = None
    quantity: Optional[float] = None
    dt_send: Optional[datetime] = None
    dt_update: Optional[datetime] = None
    dt_create: Optional[datetime] = None
    uniq_code: Optional[UUID] = None
    ean: Optional[str] = None
    group_name: Optional[str] = None
    type_product: Optional[str] = None
    product_name: Optional[str] = None
    product_producer: Optional[str] = None
    product_country: Optional[str] = None
    
    model_config = ConfigDict(from_attributes = True)
    

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
    