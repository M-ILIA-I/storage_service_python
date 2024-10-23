from .types import *



class ProductsGroup(Base):
    __tablename__ = "products_groups"
    
    id: int = Column(Integer, primary_key=True)
    parent_id: int = Column(Integer, ForeignKey("products_groups.id"))
    name: str = Column(String, nullable=False)
    formula: str = Column(String, nullable=True)