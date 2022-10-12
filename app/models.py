"""
Holds SQLAlchemy models
"""

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    authors = relationship("Author", back_populates="addedby")
    books = relationship("Book", back_populates="owner")

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    genre = Column(ARRAY(String), nullable=False)
    addedby_id = Column(Integer, ForeignKey="Users")

    addedby = relationship("User", back_populates="authors")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(ARRAY(String), ForeignKey("authors.id"))
    rating = Column(Float, default=1.0)
    genre = Column(ARRAY(String), nullable=False)
    numberofpages = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="owner")
    authors = relationship("Author", back_populates="authors")

