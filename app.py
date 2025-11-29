from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import SessionLocal, Author, Book

def create_data(db: Session):
    print("--- CREATING DATA ---")
    # 1. Create Authors
    author1 = Author(name="J.K. Rowling", birth_date=date(1965, 7, 31), nationality="British")
    author2 = Author(name="George Orwell", birth_date=date(1903, 6, 25), nationality="British")

    # 2. Create Books (associated with authors)
    book1 = Book(title="Harry Potter and the Philosopher's Stone", genre="Fantasy", isbn="978-0747532743", publication_date=date(1997, 6, 26), author=author1)
    book2 = Book(title="1984", genre="Dystopian", isbn="978-0451524935", publication_date=date(1949, 6, 8), author=author2)
    book3 = Book(title="Animal Farm", genre="Satire", isbn="978-0451526342", publication_date=date(1945, 8, 17), author=author2)

    # 3. Add to session
    # Note: Adding the books automatically adds the authors because of the relationship
    db.add_all([book1, book2, book3])
    
    # 4. Commit changes
    db.commit()
    print("Created Authors and Books successfully.")

def read_data(db: Session):
    print("\n--- READING DATA ---")
    # 1. Simple Select
    authors = db.query(Author).all()
    for author in authors:
        print(f"Author: {author.name} ({author.nationality})")
        # Accessing related books (Lazy loading)
        for book in author.books:
            print(f"  - Wrote: {book.title} ({book.genre})")

    # 2. Filtering
    print("\n[Filtering] Finding '1984':")
    dystopian_book = db.query(Book).filter(Book.title == "1984").first()
    if dystopian_book:
        print(f"Found: {dystopian_book.title} by {dystopian_book.author.name}")

def update_data(db: Session):
    print("\n--- UPDATING DATA ---")
    # 1. Fetch the record
    author_to_update = db.query(Author).filter(Author.name == "J.K. Rowling").first()
    
    if author_to_update:
        # 2. Modify the attribute
        print(f"Old Name: {author_to_update.name}")
        author_to_update.name = "Joanne Rowling" # Changing name
        
        # 3. Commit
        db.commit()
        
        # Verify
        updated_author = db.query(Author).filter(Author.id == author_to_update.id).first()
        print(f"New Name: {updated_author.name}")

def delete_data(db: Session):
    print("\n--- DELETING DATA ---")
    # 1. Find the book to delete
    book_to_delete = db.query(Book).filter(Book.title == "Animal Farm").first()
    
    if book_to_delete:
        print(f"Deleting book: {book_to_delete.title}")
        
        # 2. Delete
        db.delete(book_to_delete)
        
        # 3. Commit
        db.commit()
        print("Deletion committed.")

def main():
    db = SessionLocal()
    try:
        # Run CRUD operations
        create_data(db)
        read_data(db)
        update_data(db)
        delete_data(db)
        read_data(db)  # Verify deletion
    finally:
        db.close()

if __name__ == "__main__":
    main()


# ### How to Run the CRUD Script

# Run the python file in your terminal:


# python crud_practice.py
# ```

# ## Summary of what you learned:
# 1.  **Models:** How to create relationships (`ForeignKey`, `relationship`) and different types (`Date`, `String`).
# 2.  **Migrations:** How to use Alembic to create the initial DB and then *update* it (adding `nationality`) without losing data.
# 3.  **CRUD:** How to use the `Session` to add, query, modify, and remove objects.