from .types import *
from .partner import Partner

class TypeDocument(enum.Enum):
    INCOME = 1
    EXPENSE = 2
    ORDER = 3
    REVALUATION = 4


class Document(Base):
    __tablename__ = "documents"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True)
    partner_id: int = Column(Integer, ForeignKey("partners.id"), index=True)
    type_document: TypeDocument = Column("type_document", Enum(TypeDocument))
    useredited_id: int = Column(Integer, index=True)
    serdocument: str = Column(String)
    numdocument: str = Column(String)
    dtexecute: datetime = Column(TIMESTAMP)
    dtdocument: datetime = Column(TIMESTAMP)
    numdocumentsrc: str = Column(String)
    
    partner: Mapped[Partner] = relationship(Partner)
    