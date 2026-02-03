from pathlib import Path
from typing import Generator

from markitdown import MarkItDown

from config import BooksConfig


def parse_to_md(book_path: str) -> Generator[tuple[str, str], None, None]:
    path = Path(book_path)

    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {book_path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Expected directory, got file: {book_path}")

    md_converter = MarkItDown()

    for book in path.glob(BooksConfig.BOOK_FILE_EXTENSION.value):
        try:
            result = md_converter.convert(str(book))
            yield (book.name, result.text_content)
        except Exception as ParseError:
            print(f"Error parsing {book.name}: {ParseError}")
            continue


if __name__ == "__main__":
    for filename, markdown in parse_to_md(BooksConfig.BOOKS_DIR.value):
        print(f"Parsed: {filename}")
        print(f"Content length: {len(markdown)} characters\n")
