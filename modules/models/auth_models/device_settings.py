from ..types import *
from .device import Device


class DeviceSetting(Base):
    __tablename__ = "device_settings"
    
    id: int = Column(Integer, primary_key=True)
    device_id: int = Column(Integer, ForeignKey("devices.id"))
    name: str = Column(String)
    value: str = Column(String)
    type_value: TypeValue = Column("type_value", Enum(TypeValue))
    
    device: Mapped[Device] = relationship(Device)