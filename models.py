from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

# Define the Database URL
DATABASE_URL = "sqlite:///library.db"

# Create the Engine
engine = create_engine(DATABASE_URL, echo=False)

# create a Session Factory
SessionLocal = sessionmaker(bind=engine)

# define the Base class
Base = declarative_base()


# table definations
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    birth_date = Column(Date)
    nationality = Column(String(50))

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(name='{self.name}', nationality='{self.nationality}')>"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50))
    isbn = Column(String(20), unique=True)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title='{self.title}', isbn='{self.isbn}')>"
