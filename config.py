from enum import Enum


class BooksConfig(Enum):
    """Configuration for book downloading and processing"""

    CSV_URL = "https://raw.githubusercontent.com/alexeygrigorev/ai-engineering-buildcamp-code/main/01-foundation/homework/books.csv"
    DATA_DIR = "./data"
    BOOKS_DIR = "./data/books"
    MARKDOWN_DIR = "./books_text"
    BOOK_FILE_EXTENSION = "*.pdf"
