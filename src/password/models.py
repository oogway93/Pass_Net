from sqlalchemy import String, Column, Integer, Table

from src.database import metadata, Base


class Password(Base):
    __tablename__ = 'Password'

    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
