from .types import *
from .partner import Partner

class TypeDocument(enum.Enum):
    INCOME = 1
    EXPENSE = 2
    ORDER = 3
    REVALUATION = 4
    
    @classmethod
    def get_name(cls, value):
        for member in cls:
            if member.value == value:
                return member.name
        return None


class DocumentState(enum.Enum):
    INITIAL = 1
    PENDING = 2
    ON_DEVICE = 3
    FROM_DEVICE = 4
    DONE = 5


class Document(Base):
    __tablename__ = "documents"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, index=True, nullable=False)
    partner_id: int = Column(Integer, ForeignKey("partners.id"), index=True)
    type_document: TypeDocument = Column("type_document", Enum(TypeDocument), nullable=False)
    state: DocumentState = Column("document_state", Enum(DocumentState), nullable=False)
    user_edited_id: int = Column(Integer, index=True, nullable=False)
    comment_device: str = Column(String, nullable=True)
    photo_device: str = Column(String, comment="Путь к файлу", nullable=True)
    ser_document: str = Column(String)
    num_document: str = Column(String)
    dt_execute: datetime = Column(TIMESTAMP)
    dt_document: datetime = Column(TIMESTAMP)
    num_document_src: str = Column(String)
    
    partner: Mapped[Partner] = relationship(Partner)
    