from .types import *
from .products_name import ProductsName
from .products_producer import ProductsProducer
from .products_country import ProductsCountry


class Nomenclature(Base):
    __tablename__ = "nomenclature"
    
    id: int = Column(Integer, primary_key=True)
    name_id: int = Column(Integer, ForeignKey("products_name.id", ondelete="cascade", onupdate="cascade"))
    producer_id: int = Column(Integer, ForeignKey("products_producer.id", ondelete="cascade", onupdate="cascade"))
    country_id: int = Column(Integer, ForeignKey("products_country.id", ondelete="cascade", onupdate="cascade"))
    
    name: Mapped[ProductsName] = relationship(ProductsName)
    produser: Mapped[ProductsProducer] = relationship(ProductsProducer)
    country: Mapped[ProductsCountry] = relationship(ProductsCountry)