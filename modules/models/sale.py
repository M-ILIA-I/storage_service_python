from .types import *
from .batch import Batch


class TypeOperation(enum.Enum):
    SALE = 1
    REFUND = 2
    EXCHANGE = 3
    
class Sale(Base):
    __tablename__ = "sales"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, nullable=False)
    batch_id: int = Column(Integer, ForeignKey("batches.id"), nullable=False)
    type_operation: TypeOperation = Column('type_operation', Enum(TypeOperation), nullable=False, comment="1 - Продажа, 2 - Возврат, 3 - Обмен")
    check_number: int = Column(Integer, nullable=False)
    date_sale: datetime = Column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)
    number_sold: float = Column(Double, nullable=False)
    price_sold: float = Column(Double, nullable=False)
    discount_sum: float = Column(Double, nullable=False)
    is_send: bool = Column(Boolean, nullable=False)
    mark_uniq_code: uuid = Column(Uuid, nullable=False)
    
    batch: Mapped[Batch] = relationship(Batch)