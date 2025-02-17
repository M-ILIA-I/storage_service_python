from ..types import *
from .firm import Firm


class Store(Base):
    __tablename__ = "stores"
    
    id: int = Column(Integer, primary_key=True)
    firm_id: int = Column(Integer, ForeignKey("firms.id", ondelete="cascade", onupdate="cascade"))
    name: str = Column(String, nullable=False)
    info: str = Column(String, nullable=True)
    
    firm: Mapped[Firm] = relationship(Firm)