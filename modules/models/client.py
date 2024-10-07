from .types import *
from .city import City

    
class Client(Base):
    __tablename__ = "clients"
    
    id: int = Column(Integer, primary_key=True)
    full_name: str = Column(String)
    phone_number: str = Column(String)
    date_birthday: datetime = Column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id", ondelete="cascade", onupdate="cascade"), default=None)
    
    city: Mapped[City] = relationship(City)