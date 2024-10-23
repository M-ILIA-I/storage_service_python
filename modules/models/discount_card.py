from .types import *
from .client import Client
from .discount import Discount


class DiscountCard(Base):
    __tablename__ = "discount_cards"
    __table_args__ = (
        UniqueConstraint('id', 'client_id', name='uq_id_client_id'),
    )
    
    id: int = Column(Integer, primary_key=True)
    client_id: int = Column(Integer, ForeignKey("clients.id", ondelete="cascade", onupdate="cascade"), nullable=False)
    discount_id: int = Column(Integer, ForeignKey("discounts.id", ondelete="cascade", onupdate="cascade"), nullable=False)
    number_card: str = Column(String, nullable=False)
    amount_bonuses: float = Column(Double, nullable=False)
    amount_checks: int = Column(Integer, nullable=False)
    number_chacks: int = Column(Integer, nullable=False)
    
    client: Mapped[Client] = relationship(Client)
    discount: Mapped[Discount] = relationship(Discount)