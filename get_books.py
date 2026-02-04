import csv
import os
from pathlib import Path
from typing import Generator
from urllib.request import urlopen

from config import BooksConfig


def download_books_csv(csv_url: str, output_dir: str) -> str:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        filename = os.path.join(output_dir, "books.csv")
        with urlopen(csv_url) as response:
            with open(filename, "wb") as out_file:
                out_file.write(response.read())
        print(f"\nCSV downloaded successfully to {filename}")
        return filename
    except Exception as DownloadError:
        print(f"\nError downloading CSV: {DownloadError}")
        return None


def download_all_books(csv_path: str, output_dir: str) -> bool:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                book_url = row["pdf_url"]
                try:
                    filename = os.path.basename(book_url)
                    filepath = os.path.join(output_dir, filename)
                    with urlopen(book_url) as response:
                        with open(filepath, "wb") as out_file:
                            out_file.write(response.read())
                    print(f"\nDownloaded: {filename}")
                except Exception as e:
                    print(f"\nFailed to download {book_url}: {e}")
        return True
    except Exception as ProcessError:
        print(f"\nError processing CSV: {ProcessError}")
        return False


def get_book_files(output_dir: str) -> Generator[Path, None, None]:
    try:
        for book_path in Path(output_dir).glob(BooksConfig.BOOK_FILE_EXTENSION.value):
            yield book_path
    except Exception as IterationError:
        print(f"\nError iterating files: {IterationError}")
