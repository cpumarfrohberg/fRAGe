# Book Processing CLI

CLI tool for downloading and parsing technical books to Markdown format.

## Features

- Download books from CSV file
- Parse PDF books to Markdown using MarkItDown
- Clean CLI interface with Typer

## Installation

```bash
uv sync
```

## Usage

### Download books

```bash
uv run books download
```

### Parse books to Markdown

```bash
uv run books parse
uv run books parse --output-dir ./markdown
uv run books parse --no-save  # Preview only
```

### Help

```bash
uv run books --help
uv run books download --help
uv run books parse --help
```

## Project Structure

```
.
├── cli.py           # Typer CLI commands
├── get_books.py     # Book downloading logic
├── parse_to_md.py   # PDF parsing logic
└── pyproject.toml   # Project configuration
```

## Requirements

- Python >= 3.11
- See `pyproject.toml` for dependencies
