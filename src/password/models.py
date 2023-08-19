from sqlalchemy import String, Column, Integer

from src.database import Base


class Password(Base):
    """Class Password"""
    __tablename__ = 'Password'

    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
