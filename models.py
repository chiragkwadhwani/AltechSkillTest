from sqlalchemy import Column, ForeignKey, Integer, String, Date
from database import Base


class Author(Base):
    __tablename__ = "Authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, index=True)
    bio = Column(String(255))
    birth_date = Column(String(10))


class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    publish_date = Column(String(10))
    author_id = Column(Integer, ForeignKey("Authors.id"))
