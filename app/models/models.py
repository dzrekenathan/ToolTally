from sqlalchemy import TIMESTAMP, String, Boolean, Integer, Column, text
from ..core.database import Base



class User(Base):
    __tablename__ = "users"

    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False, server_default=text('False'))
    status = Column(String, nullable=False, server_default='ENABLED')
    date_created = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)