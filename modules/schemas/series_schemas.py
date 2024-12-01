from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional


class SeriesSchema(BaseModel):
    id: Optional[int] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    batch_id: Optional[int] = None
    document_id: Optional[int] = None
    partner_short_name: Optional[str] = None
    dt_expiration: Optional[datetime] = None
    num_came: Optional[float] = None
    num_rest: Optional[float] = None
    price_ro: Optional[float] = None
    perc_ws: Optional[float] = None
    price_ws: Optional[float] = None
    perc_nds_in: Optional[float] = None
    perc_rozn: Optional[float] = None
    perc_nds: Optional[float] = None
    price_full: Optional[float] = None
    product_country: Optional[str] = None
    product_name: Optional[str] = None
    product_producer: Optional[str] = None
    product_group: Optional[str] = None
    ean: Optional[str] = None
    
    model_config = ConfigDict(from_attributes = True)
    
class GetSeriesResponseSchema(BaseModel):
    status: str
    code: int
    data: List[SeriesSchema]