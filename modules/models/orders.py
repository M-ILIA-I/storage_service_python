from .types import *
from .series import Series
from .document import Document


class Order(Base):
    __tablename__ = "docs_elems_orders"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True, nullable=False)
    document_id: int = Column(Integer, ForeignKey("documents.id"))
    serie_id: int = Column(Integer, ForeignKey("docs_elems_series.id"), index=True)
    num_order: int = Column(Integer, nullable=False)
    
    document: Mapped[Document] = relationship(Document)
    serie: Mapped[Series] = relationship(Series)