from ..types import *
from .firm import Firm


class FirmSetting(Base):
    __tablename__ = "firm_settings"
    
    id: int = Column(Integer, primary_key=True)
    firm_id: int = Column(Integer, ForeignKey("firms.id", ondelete="cascade", onupdate="cascade"))
    name: str = Column(String)
    value: str = Column(String)
    type_value: TypeValue = Column("type_value", Enum(TypeValue))
    
    firm: Mapped[Firm] = relationship(Firm)