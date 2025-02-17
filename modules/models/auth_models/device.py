from ..types import *
from .store import Store


class Device(Base):
    __tablename__ = "devices"
    
    id: int = Column(Integer, primary_key=True)
    store_id: int = Column(Integer, ForeignKey("stores.id", ondelete="cascade", onupdate="cascade"))
    name: str = Column(String)
    username: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    sold: str = Column(String)
    info: str = Column(String)
    
    store: Mapped[Store] = relationship(Store)
        
    