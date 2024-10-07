from .types import *


class TypeOperation(enum.Enum):
    SALE = 1
    REFUND = 2
    EXCHANGE = 3
    
class Sale(Base):
    __tablename__ = "sales"
    
    id: int = Column(Integer, primary_key=True)
    batch_id: int = Column(Integer)
    type_operation: TypeOperation = Column('type_operation', Enum(TypeOperation), comment="1 - Продажа, 2 - Возврат, 3 - Обмен")
    check_number: int = Column(Integer)
    date_sale: datetime = Column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)
    number_sold: float = Column(Double)
    price_sold: float = Column(Double)
    discount_sum: float = Column(Double)
    is_send: bool = Column(Boolean)
    mark_uniq_code: uuid = Column(Uuid)