"""Console script for data_vista."""
import data_vista

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for data_vista."""
    console.print("Replace this message by putting your code into "
               "data_vista.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
