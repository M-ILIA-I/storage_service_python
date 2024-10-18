from .types import *
from .document import Document


class Work(Base):
    __tablename__ = "docs_elems_work"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True)
    document_id: int = Column(Integer, ForeignKey("documents.id"))
    
    document: Mapped[Document] = relationship(Document)