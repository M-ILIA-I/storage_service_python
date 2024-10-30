from ..types import *


class Firm(Base):
    __tablename__ = "firms"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, index=True)
    info: str = Column(String)