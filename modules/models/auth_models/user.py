from ..types import * 
from .firm import Firm

class User(Base):
    __tablename__ = "users"
    
    id: int = Column(Integer, primary_key=True)
    firm_id: int = Column(Integer , ForeignKey("firms.id", ondelete="cascade", onupdate="cascade"))
    username: str = Column(String, index=True, unique=True)
    password: str = Column(String)
    sold: int = Column(Integer)
    permissions: str = Column(String)