# fRAGe - Question Answering System

A Retrieval-Augmented Generation (RAG) system for querying book contents using semantic search and LLMs.

## Features

- ✅ Download technical books from CSV
- ✅ Parse PDF books to Markdown
- 🚧 Semantic search over book contents (TODO)
- 🚧 Ask questions and get answers from books (TODO)
- 🚧 LLM-powered responses with source citations (TODO)

## Installation

```bash
uv sync
```

## Commands

**Download books:**
```bash
uv run books download [--books-dir PATH]
```

**Parse PDFs to markdown:**
```bash
uv run books parse [--output-dir PATH] [--no-save]
```
- Default saves to `./books_text/`
- Use `--no-save` to preview line/character counts without saving


## Requirements

- Python >= 3.11
- OpenAI API key (for RAG features - TODO)
- See `pyproject.toml` for dependencies
