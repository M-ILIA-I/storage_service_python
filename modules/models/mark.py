from .types import *
from .batch import Batch


class TypeMark(enum.Enum):
    UKZ = 1
    SI = 2
    

class Mark(Base):
    __tablename__ = "marks"
    
    id: int = Column(Integer, primary_key=True)
    batch_id: int = Column(Integer, ForeignKey("batches.id", ondelete="cascade", onupdate="cascade"))
    uniq_code: uuid = Column(Uuid, nullable=False)
    value: str = Column(String, nullable=False)
    type_mark: TypeMark = Column("type_mark", Enum(TypeMark), nullable=False)
    is_sold: bool = Column(Boolean, nullable=False)
    # dt_send: datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    # dt_update: datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    # dt_create: datetime = Column(TIMESTAMP, nullable=False, server_default=func.now())
    
    batch: Mapped[Batch] = relationship(Batch)