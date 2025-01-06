from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DID(Base):
    __tablename__ = "dids"

    id = Column(Integer, primary_key=True, index=True)
    did = Column(String(191), unique=True, nullable=False)
    controller = Column(String(191), nullable=False)
    document = Column(Text, nullable=False)  # Cambiar el tipo a Text para almacenar JSON
