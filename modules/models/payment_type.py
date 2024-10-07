from .types import *


class PaymentType(Base):
    __tablename__ = "payment_types"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    cash_payment_id: int = Column(Integer)
    cash_name: str = Column(String)