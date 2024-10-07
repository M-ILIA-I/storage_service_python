from .types import *


class ProductsName(Base):
    __tablename__ = "products_name"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)