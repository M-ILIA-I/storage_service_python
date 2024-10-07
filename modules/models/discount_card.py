from .types import *
from .client import Client
from .discount import Discount


class DiscountCard(Base):
    __tablename__ = "discount_cards"
    __table_args__ = (
        UniqueConstraint('id', 'client_id', name='uq_id_client_id'),
    )
    
    id: int = Column(Integer, primary_key=True)
    client_id: int = Column(Integer, ForeignKey("clients.id", ondelete="cascade", onupdate="cascade"))
    discount_id: int = Column(Integer, ForeignKey("discounts.id", ondelete="cascade", onupdate="cascade"))
    number_card: str = Column(String)
    amount_bonuses: float = Column(Double)
    amount_checks: int = Column(Integer)
    number_chacks: int = Column(Integer)
    
    client: Mapped[Client] = relationship(Client)
    discount: Mapped[Discount] = relationship(Discount)