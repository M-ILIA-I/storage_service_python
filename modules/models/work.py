from .types import *
from .document import Document
    

class Work(Base):
    __tablename__ = "docs_elems_work"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True, nullable=False)
    document_id: int = Column(Integer, ForeignKey("documents.id", ondelete="cascade"))
    row_number: int = Column(Integer, nullable=False)
    col_name: str = Column(String, nullable=False)
    col_value: str = Column(String, nullable=False)
    type_value: TypeValue = Column("type_value", Enum(TypeValue), nullable=False)
    dt_change: datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    document: Mapped[Document] = relationship(Document)