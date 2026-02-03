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

Set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-key-here"
```

Or create a `.env` file:

```
OPENAI_API_KEY=your-key-here
```

## Quick Start

```bash
# 1. Download books
uv run books download

# 2. Parse to markdown
uv run books parse

# TODO: RAG features coming soon
# 3. Index books for RAG
# uv run books index

# 4. Ask questions
# uv run books ask "What is a list comprehension in Python?"
```

## Usage

### Download books

```bash
uv run books download
uv run books download --books-dir ./custom/path
```

### Parse books to Markdown

```bash
uv run books parse
uv run books parse --output-dir ./markdown
```

### Index books for search (TODO)

```bash
# Coming soon
# uv run books index
# uv run books index --chunk-size 1000
```

### Ask questions (TODO)

```bash
# Coming soon
# uv run books ask "How do I use decorators in Python?"
# uv run books ask "Explain recursion" --top-k 5
```

### Interactive mode (TODO)

```bash
# Coming soon
# uv run books chat
```


## Requirements

- Python >= 3.11
- OpenAI API key (for RAG features - TODO)
- See `pyproject.toml` for dependencies
