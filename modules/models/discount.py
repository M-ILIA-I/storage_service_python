from .types import *


class TypeDiscount(enum.Enum):
    MANUAL = 1
    AUTO = 2
    

class Discount(Base):
    __tablename__ = "discounts"
    
    id: int = Column(Integer, primary_key=True)
    type_discount: TypeDiscount = Column('type_discount', Enum(TypeDiscount), comment="1 - Ручная, 2 -Автоматическая")
    namme: str = Column(String)
    value: float = Column(Double)
    rule: str = Column(String)