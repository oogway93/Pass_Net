from sqlalchemy import MetaData, Boolean, String, Column, Integer, Table

from src.password.database import Base

metadata = MetaData()

password = Table(
    "Password",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("password", String),
)





# class Password(Base):
#     __tablename__ = 'Password'
#
#     id = Column(Integer, primary_key=True, nullable=False)
#     password = Column(String, nullable=False)
#     length = Column(Integer, nullable=False)
#     uppercase_chars = Column(Boolean, default=False)
#     digits = Column(Boolean, default=False)
#     special_chars = Column(Boolean, default=False)
#     hard_mode = Column(Boolean, default=False)


