from ..types import *


class InvoiceParams(Base):
    __tablename__ = "invoice_params"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    parse_value: str = Column(String, nullable=False)