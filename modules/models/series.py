from .types import *
from .batch import Batch
from .document import Document


class Series(Base):
    __tablename__ = "docs_elems_series"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True)
    batch_id: int = Column(Integer, ForeignKey("batches.id"), index=True)
    document_id: int = Column(Integer, ForeignKey("documents.id"), index=True)
    dt_expiration: datetime = Column(TIMESTAMP)
    num_came: float = Column(Double)
    num_rest: float = Column(Double)
    price_ro: float = Column(Double)
    perc_ws: float = Column(Double)
    price_ws: float = Column(Double)
    perc_nds_in: float = Column(Double)
    perc_rozn: float = Column(Double)
    perc_nds: float = Column(Double)
    price_full: float = Column(Double)
    
    batch: Mapped[Batch] = relationship(Batch)
    document: Mapped[Document] = relationship(Document)