from sqlalchemy import Boolean, String, Column, Integer


class Password(Base):
    __tablename__ = 'Password'

    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    uppercase_chars = Column(Boolean, default=False)
    digits = Column(Boolean, default=False)
    special_chars = Column(Boolean, default=False)
    hard_mode = Column(Boolean, default=False)


