from .types import *


class PaymentType(Base):
    __tablename__ = "payment_types"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    cash_payment_id: int = Column(Integer, nullable=False)
    cash_name: str = Column(String, nullable=False)