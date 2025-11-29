# Library Management System

A simple library management system built with SQLAlchemy and Alembic, demonstrating database operations with authors and books.

## Features

- **Database Models**: Authors and Books with relationships
- **CRUD Operations**: Create, Read, Update, Delete records
- **Database Migrations**: Version-controlled schema changes with Alembic
- **SQLite Database**: Lightweight, file-based database

## Project Structure

```
.
├── models.py          # SQLAlchemy models for Authors and Books
├── app.py             # Main application with CRUD operations
├── alembic/           # Database migration files
│   ├── versions/      # Individual migration scripts
│   └── alembic.ini    # Alembic configuration
├── Pipfile            # Python dependencies
├── Pipfile.lock       # Locked dependencies
├── library.db         # SQLite database (created after setup)
└── README.md          # This file
```

## Database Schema

### Authors Table
- `id` (Integer, Primary Key)
- `name` (String, 50 chars, Not Null)
- `birth_date` (Date)
- `nationality` (String, 50 chars)

### Books Table
- `id` (Integer, Primary Key)
- `title` (String, 100 chars, Not Null)
- `genre` (String, 50 chars)
- `isbn` (String, 20 chars, Unique)
- `publication_date` (Date)
- `author_id` (Integer, Foreign Key to Authors)

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pipenv (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd library
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

4. **Set up the database:**
   ```bash
   # Initialize/upgrade database to latest migration
   alembic upgrade head
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

### Setting up SQLAlchemy and Alembic from Scratch

If starting a new project, here's how to set up SQLAlchemy and Alembic:

1. **Install SQLAlchemy and Alembic:**
   ```bash
   pipenv install sqlalchemy alembic
   ```

2. **Initialize Alembic (creates alembic/ directory and alembic.ini):**
   ```bash
   alembic init alembic
   ```

3. **Configure database URL in `alembic.ini`:**
   Edit `alembic.ini` and set:
   ```ini
   sqlalchemy.url = sqlite:///your_database.db
   ```

4. **Create initial migration (after defining models in models.py):**
   ```bash
   alembic revision --autogenerate -m "initial setup"
   ```

5. **Apply migration to create database tables:**
   ```bash
   alembic upgrade head
   ```

6. **For future model changes:**
   - Modify your models in `models.py`
   - Generate new migration: `alembic revision -m "describe changes"`
   - Apply changes: `alembic upgrade head`

### Alembic Commands Reference

- **Check current migration status:** `alembic current`
- **View migration history:** `alembic history`
- **Create new migration:** `alembic revision -m "message"`
- **Apply all pending migrations:** `alembic upgrade head`
- **Rollback migrations:** `alembic downgrade -1` (or specific revision)

## What the Application Does

The `app.py` script demonstrates:

1. **Creating Data**: Adds sample authors (J.K. Rowling, George Orwell) and their books
2. **Reading Data**: Queries and displays all authors with their books, plus filtered searches
3. **Updating Data**: Modifies an author's name
4. **Deleting Data**: Removes a book from the database

## Database Migrations

The project uses Alembic for database version control. Migration files are located in `alembic/versions/`:

- Initial table creation
- Adding nationality to authors
- Adding genre to books
- Various updates and fixes

To create a new migration after model changes:
```bash
alembic revision -m "description of changes"
alembic upgrade head
```

## Dependencies

- SQLAlchemy: ORM for database operations
- Alembic: Database migration tool

## Development Notes

- Database: SQLite (`library.db`)
- All migrations are applied automatically on setup
- The application creates sample data on each run
- For production use, consider using a more robust database like PostgreSQL

## Troubleshooting

- If you encounter database errors, try deleting `library.db` and re-running `alembic upgrade head`
- Ensure you're in the pipenv virtual environment when running commands
- Check that Python 3.8+ is installed

## License

[Add your license information here]