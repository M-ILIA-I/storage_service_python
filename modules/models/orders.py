from .types import *
from .series import Series
from .document import Document


class Order(Base):
    __tablename__ = "docs_elems_orders"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True)
    document_id: int = Column(Integer, ForeignKey("documents.id"))
    docs_elems_series_id: int = Column(Integer, ForeignKey("docs_elems_series.id"), index=True)
    numorder: int = Column(Integer)
    
    document: Mapped[Document] = relationship(Document)
    docs_elems_series: Mapped[Series] = relationship(Series)