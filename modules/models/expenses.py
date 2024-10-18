from .types import *
from .document import Document
from .series import Series


class Expenses(Base):
    __tablename__ = "docs_elems_expenses"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True)
    document_id: int = Column(Integer, ForeignKey("documents.id"), index=True)
    docs_elems_series_id: int = Column(Integer, ForeignKey("docs_elems_series.id"))
    dtform: datetime = Column(TIMESTAMP)
    numreserve: int = Column(Integer)
    useredited_id: int = Column(Integer)
    
    document: Mapped[Document] = relationship(Document)
    docs_elems_series: Mapped[Series] = relationship(Series)
    