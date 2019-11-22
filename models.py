from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
#describes what variables will be in the table: id, name, etc.
class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())
