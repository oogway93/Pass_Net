from sqlalchemy import Column, Integer

from src.database import Base


class PinCode(Base):
    """Class Pin Code"""
    __tablename__ = "Pin-Code"

    id = Column(Integer, primary_key=True, nullable=False)
    pin = Column(Integer, nullable=False)
