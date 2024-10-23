from .types import *


class Batch(Base):
    __tablename__ = "batches"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, nullable=False, index=True)
    product_id: int = Column(Integer, ForeignKey("products.id", ondelete="cascade", onupdate="cascade"), nullable=False, index=True)
    price: float = Column(Double, nullable=False)
    quantity: float = Column(Double)
    dt_send: datetime = Column(TIMESTAMP, nullable=False)
    dt_update: datetime = Column(TIMESTAMP, nullable=False)
    dt_create: datetime = Column(TIMESTAMP, nullable=False)
    
    