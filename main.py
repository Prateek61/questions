import typer
from rich import print as rprint
import os
import markdownify
from pathlib import Path

from modules.helper import *

from typing_extensions import Annotated

# Main typer app
app = typer.Typer()

# Subcommands
@app.command()
def scan() -> None:
    """Scans """
    rprint("[bold green]Scanning...[/bold green]")

@app.command()
def parse(
    folder_path: Annotated[Path, typer.Argument(..., help="Path to the folder the files are in", exists=True, )],
    show: bool = typer.Option(True, help="Saves the parsed files to test folder"),
    push: bool = typer.Option(False, help="Pushes the parsed files to database"),
    remove_tags: bool = typer.Option(False, help="Removes all tags except <p> and <img> tags")
) -> None:
    """Parse and push the files to database"""
    soup = html_body_from_file(folder_path)
    if remove_tags:
        remove_tags_except_p_and_img(soup)
    
    if show:
        # Save the parsed file to test folder
        with open(Path("test/parsed.html"), "w") as f:
            f.write(str(soup))
        rprint("[bold green]Parsed file saved to test/parsed.html[/bold green]")

    markdown = markdownify.markdownify(str(soup))
    if show:
        # Save the parsed file to test folder
        with open(Path("test/parsed.md"), "w") as f:
            f.write(markdown)
        rprint("[bold green]Parsed file saved to test/parsed.md[/bold green]")

    if push:
        # Push the parsed file to database
        rprint("[bold red]Pushing to database not implemented yet[/bold red]")



if __name__ == "__main__":
    app()