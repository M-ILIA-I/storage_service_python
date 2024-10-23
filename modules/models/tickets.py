from .types import *
from .client import Client
from .discount import Discount
from .batch import Batch


class TypeTicket(enum.Enum):
    OPEN = 1
    CLOSE = 2
    DELAY = 3
    
    
class Ticket(Base):
    __tablename__ = "tickets"
    
    id: int = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id", ondelete="cascade", onupdate="cascade"), nullable=False, index=True)
    client_id: int = Column(Integer, ForeignKey("clients.id", ondelete="cascade", onupdate="cascade"), index=True)
    discount_id: int = Column(Integer, ForeignKey("discounts.id", ondelete="cascade", onupdate="cascade"), index=True)
    type_ticket: TypeTicket = Column('type_ticket', Enum(TypeTicket), nullable=False, comment="1 - Открыт, 2 - Закрыт, 3 - Удержан")
    quantity: float = Column(Double, nullable=False)
    
    client: Mapped[Client] = relationship(Client)
    discount: Mapped[Discount] = relationship(Discount)
    batches: Mapped[Batch] = relationship(Batch)
    
    