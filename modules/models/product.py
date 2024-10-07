from .types import *
from .nomenclature import Nomenclature


class TypeProduct(enum.Enum):
    PRODUCT = 1
    SERVICE = 2
    

class Product(Base):
    __tablename__ = "products"
    
    id: int = Column(Integer, primary_key=True)
    nomenclature_id: int = Column(Integer, ForeignKey("nomenclature.id", ondelete="cascade", onupdate="cascade"))
    ean: str = Column(String)
    type_product: TypeProduct = Column("type_product", Enum(TypeProduct), comment="1 - продукт, 2 - услуга")
    
    nomenclature: Mapped[Nomenclature] = relationship(Nomenclature)