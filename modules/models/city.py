from .types import *
    
    
class City(Base):
    __tablename__ = "cities"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    