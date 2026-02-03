import os
import typer
from typing import Optional

from get_books import download_books_csv, download_all_books, CSV_URL, DATA_DIR, BOOKS_DIR
from parse_to_md import parse_to_md

app = typer.Typer(help='Book processing CLI for AI Bootcamp Week 2')


@app.command()
def download(
    csv_url: str = typer.Option(CSV_URL, help='URL to books CSV file'),
    data_dir: str = typer.Option(DATA_DIR, help='Directory to save CSV'),
    books_dir: str = typer.Option(BOOKS_DIR, help='Directory to save books')
):
    """Download books from CSV."""
    typer.echo(f'📥 Downloading books CSV from {csv_url}...')
    
    csv_path = download_books_csv(csv_url, data_dir)
    
    if csv_path:
        typer.echo(f'✓ CSV downloaded to {csv_path}')
        typer.echo(f'\n📚 Downloading all books to {books_dir}...')
        
        if download_all_books(csv_path, books_dir):
            typer.echo('✓ All books downloaded successfully!')
        else:
            typer.echo('⚠️  Some books may have failed to download', err=True)
    else:
        typer.echo('✗ Failed to download CSV', err=True)
        raise typer.Exit(code=1)


@app.command()
def parse(
    books_dir: str = typer.Option(BOOKS_DIR, help='Directory containing PDF books'),
    output_dir: Optional[str] = typer.Option('./data/markdown', help='Output directory for markdown files'),
    save: bool = typer.Option(True, help='Save markdown to files'),
    preview_length: int = typer.Option(500, help='Preview length in characters (when not saving)')
):
    """Parse PDF books to Markdown."""
    typer.echo(f'📖 Parsing books from {books_dir}...\n')
    
    if save and output_dir:
        os.makedirs(output_dir, exist_ok=True)
        typer.echo(f'💾 Saving markdown files to {output_dir}\n')
    
    parsed_count = 0
    
    for filename, markdown in parse_to_md(books_dir):
        md_filename = filename.replace('.pdf', '.md')
        
        if save and output_dir:
            md_path = os.path.join(output_dir, md_filename)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            typer.echo(f'✓ Saved: {md_filename} ({len(markdown):,} characters)')
        else:
            typer.echo(f'--- {filename} ---')
            typer.echo(markdown[:preview_length])
            typer.echo(f'... (total: {len(markdown):,} characters)\n')
        
        parsed_count += 1
    
    if parsed_count == 0:
        typer.echo(f'⚠️  No PDF files found in {books_dir}', err=True)
    else:
        typer.echo(f'\n✓ Parsed {parsed_count} book(s) successfully!')


if __name__ == '__main__':
    app()
