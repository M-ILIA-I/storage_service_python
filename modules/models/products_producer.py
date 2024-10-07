from .types import *


class ProductsProducer(Base):
    __tablename__ = "products_producer"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)