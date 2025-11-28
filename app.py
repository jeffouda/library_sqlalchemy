from datetime import date
from sqlalchemy.orm import Session 
from sqlalchemy import select
from models import SessionLocal, Book, Author

def create_data(db:Session):
    # Create authors
    author1 = Author(name="J.K. Rowling", birth_date=date(1965, 7, 31))
    author2 = Author(name="George Orwell", birth_date=date(1903, 6, 25))
    
    #create books
    book1 = Book(title="Harry Potter and the Philosopher's Stone", publication_date=date(1997, 6, 26), author=author1)
    book2 = Book(title="1984", publication_date=date(1949, 6, 8), author=author2)
    
    # Add to session
    db.add_all([author1, author2, book1, book2])
    db.commit()

def read_data(db:Session):
    # simple select
    authors = db.query(Author).all()
    for author in authors:
        print(f"Author: {author.name}, Birth Date: {author.birth_date}")
        for book in author.books:
            print(f"Book: {book.title} ({book.genre})")