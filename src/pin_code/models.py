from sqlalchemy import Column, Integer, String, Table

from src.database import Base, metadata


class PinCode(Base):
    __tablename__ = "Pin-Code"

    id = Column(Integer, primary_key=True, nullable=False)
    pin = Column(String, nullable=False)
