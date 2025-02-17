from .types import *


class Partner(Base):
    __tablename__ = "partners"
    
    id: int = Column(Integer, primary_key=True)
    invoice_params_id: int = Column(Integer)
    name_short: str = Column(String, nullable=False)
    name_full: str = Column(String, nullable=False)
    name_subdivision: str = Column(String)
    is_active: bool = Column(Boolean, nullable=False)
    is_inner_sale: bool = Column(Boolean, nullable=False)
    file_params_invoice: str = Column(String)
    folder_invoices: str = Column(String)
    info_unn: str = Column(String)
    info_address: str = Column(String)
    info_phones: str = Column(String)
    info_account: str = Column(String)
    info_bank: str = Column(String)
    info_bank_address: str = Column(String)
    info_bank_bik: str = Column(String)
    info_treaty: str = Column(String)
    info_treaty_create: datetime = Column(TIMESTAMP)
    info_director: str = Column(String)
    info_main_buch: str = Column(String)
    info_unloading_address: str = Column(String)