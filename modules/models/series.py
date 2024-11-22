from .types import *
from .batch import Batch
from .document import Document


class Series(Base):
    __tablename__ = "docs_elems_series"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True, nullable=False)
    batch_id: int = Column(Integer, ForeignKey("batches.id"), index=True, nullable=False)
    document_id: int = Column(Integer, ForeignKey("documents.id", ondelete="cascade"), index=True, nullable=False)
    dt_expiration: datetime = Column(TIMESTAMP, nullable=False)
    num_came: float = Column(Double, nullable=False)
    num_rest: float = Column(Double, nullable=False)
    price_ro: float = Column(Double, nullable=False)
    perc_ws: float = Column(Double, nullable=False)
    price_ws: float = Column(Double, nullable=False)
    perc_nds_in: float = Column(Double, nullable=False)
    perc_rozn: float = Column(Double, nullable=False)
    perc_nds: float = Column(Double, nullable=False)
    price_full: float = Column(Double, nullable=False)
    
    batch: Mapped[Batch] = relationship(Batch)
    document: Mapped[Document] = relationship(Document)