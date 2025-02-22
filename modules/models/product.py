from .types import *
from .products_name import ProductsName
from .products_country import ProductsCountry
from .products_producer import ProductsProducer
from .products_group import ProductsGroup


class TypeProduct(enum.Enum):
    PRODUCT = 1
    SERVICE = 2
    

class Product(Base):
    __tablename__ = "products"
    
    id: int = Column(Integer, primary_key=True)
    name_id: int = Column(Integer, ForeignKey("products_name.id"), nullable=False, index=True)
    producer_id: int = Column(Integer, ForeignKey("products_producer.id"), nullable=False, index=True)
    country_id: int = Column(Integer, ForeignKey("products_country.id"), nullable=False, index=True)
    group_id: int = Column(Integer, ForeignKey("products_groups.id"), index=True)
    ean: str = Column(String, nullable=False)
    type_product: TypeProduct = Column("type_product", Enum(TypeProduct), nullable=False, comment="1 - продукт, 2 - услуга")
    
    name: Mapped[ProductsName] = relationship(ProductsName)
    group: Mapped[ProductsGroup] = relationship(ProductsGroup)
    producer: Mapped[ProductsProducer] = relationship(ProductsProducer)
    country: Mapped[ProductsCountry] = relationship(ProductsCountry)