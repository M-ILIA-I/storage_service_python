from .types import *


class TypeDiscount(enum.Enum):
    MANUAL = 1
    AUTO = 2
    

class Discount(Base):
    __tablename__ = "discounts"
    
    id: int = Column(Integer, primary_key=True)
    type_discount: TypeDiscount = Column('type_discount', Enum(TypeDiscount), nullable=False, comment="1 - Ручная, 2 -Автоматическая")
    namme: str = Column(String, nullable=False)
    value: float = Column(Double, nullable=False)
    rule: str = Column(String, nullable=False)