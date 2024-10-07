from .types import *


class Batch(Base):
    __tablename__ = "batches"
    
    id: int = Column(Integer, primary_key=True)
    product_id: int = Column(Integer, ForeignKey("products.id", ondelete="cascade", onupdate="cascade"))
    part: int = Column(Integer)
    price: float = Column(Double)
    quantity: float = Column(Double)
    
    