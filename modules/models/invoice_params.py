from .types import * 


class InvoceParams(Base):
    __tablename__ = 'invoice_params'
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    parse_value: str = Column(String)