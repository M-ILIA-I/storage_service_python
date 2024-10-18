from .types import *


class Partner(Base):
    __tablename__ = "partners"
    
    id: int = Column(Integer, primary_key=True)
    name_short: str = Column(String)
    name_full: str = Column(String)
    name_subdivision: str = Column(String)
    isactive: bool = Column(Boolean)
    isinnersale: bool = Column(Boolean)
    fileparamsinvoice: str = Column(String)
    folderinvoices: str = Column(String)
    infounn: str = Column(String)
    infoaddress: str = Column(String)
    infophones: str = Column(String)
    infoaccount: str = Column(String)
    infobank: str = Column(String)
    infobankaddress: str = Column(String)
    infobankbik: str = Column(String)
    infotreaty: str = Column(String)
    infotreatycreate: datetime = Column(TIMESTAMP)
    infodirector: str = Column(str)
    infomainbuch: str = Column(String)
    infounloadingaddress: str = Column(String)