from .types import *
from .document import Document
from .series import Series


class Expenses(Base):
    __tablename__ = "docs_elems_expenses"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True, nullable=False)
    document_id: int = Column(Integer, ForeignKey("documents.id", ondelete="cascade"), index=True)
    serie_id: int = Column(Integer, ForeignKey("docs_elems_series.id"))
    dt_from: datetime = Column(TIMESTAMP, nullable=False)
    num_reserve: int = Column(Integer, nullable=False)
    user_edited_id: int = Column(Integer, nullable=False)
    
    document: Mapped[Document] = relationship(Document)
    serie: Mapped[Series] = relationship(Series)
    