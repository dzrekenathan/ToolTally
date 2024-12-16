from sqlalchemy import TIMESTAMP, LargeBinary, String, Boolean, Integer, Column, text
from ..core.database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"


    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    filename = Column(String, index=True)
    content_type = Column(String, nullable=True)
    data = Column(LargeBinary, nullable=True)
    published = Column(Boolean, nullable=False, server_default=text('True'))
    date_created = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    owner = relationship("User", back_populates="posts")
    


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
    owner = relationship("User", back_populates="posts")