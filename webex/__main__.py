import typer
from pathlib import Path
import logging

import auth
import locations
import analytics


logging.basicConfig(
    filename=Path('webex.log'), 
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )

app = typer.Typer()
app.add_typer(auth.app, name="auth")
app.add_typer(locations.app, name="locations")
app.add_typer(analytics.app, name="analytics")

if __name__ == "__main__":
    app()