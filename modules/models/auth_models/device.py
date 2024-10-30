from ..types import *
from .firm import Firm


class Device(Base):
    __tablename__ = "devices"
    
    id: int = Column(Integer, primary_key=True)
    firm_id: int = Column(Integer, ForeignKey("firms.id", ondelete="cascade", onupdate="cascade"))
    name: str = Column(String)
    username: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    sold: str = Column(String)
    info: str = Column(String)
    
    firm: Mapped[Firm] = relationship(Firm)
        
    