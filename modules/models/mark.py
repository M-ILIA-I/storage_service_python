from .types import *


class TypeMark(enum.Enum):
    UKZ = 1
    SI = 2
    

class Mark(Base):
    __tablename__ = "marks"
    
    id: int = Column(Integer, primary_key=True)
    batch_id: int = Column(Integer, ForeignKey("batches.id", ondelete="cascade", onupdate="cascade"))
    uniq_code: uuid = Column(Uuid)
    value: str = Column(String)
    type_mark: TypeMark = Column("type_mark", Enum(TypeMark))
    is_sold: bool = Column(Boolean)