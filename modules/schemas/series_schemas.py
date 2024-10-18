from pydantic import BaseModel
from datetime import datetime
from typing import List


class SeriesSchema(BaseModel):
    id: int | None
    device_id: int  | None
    batch_id: int  | None
    document_id: int | None
    dt_expiration: datetime | None 
    num_came: float  | None
    num_rest: float  | None
    price_ro: float  | None
    perc_ws: float  | None
    price_ws: float | None
    perc_nds_in: float  | None
    perc_rozn: float | None
    perc_nds: float  | None
    price_full: float  | None
    
    class Config():
        from_attributes = True
    
class GetSeriesResponseSchema(BaseModel):
    status: str
    code: int
    data: List[SeriesSchema]