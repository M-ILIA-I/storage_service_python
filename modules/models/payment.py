from .types import *
from .sale import Sale
from .payment_type import PaymentType


class Payment(Base):
    __tablename__ = "payments"
    
    id: int = Column(Integer, primary_key=True)
    payment_id: int = Column(Integer, ForeignKey("payment_types.id", ondelete="cascade", onupdate="cascade"))
    sale_id: int = Column(Integer, ForeignKey("sales.id", ondelete="cascade", onupdate="cascade"))
    sum_payed: float = Column(Double)
    
    sale: Mapped[Sale] = relationship(Sale)
    payment_type: Mapped[PaymentType] = relationship(PaymentType)