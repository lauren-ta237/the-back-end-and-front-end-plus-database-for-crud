from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# creating a database table for users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(50))

#  creating a database table for posts
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(String(100), nullable=False)
    user_id = Column(Integer, nullable=False)