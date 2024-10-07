from .types import *


class ProductsCountry(Base):
    __tablename__ = "products_country"
    
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)