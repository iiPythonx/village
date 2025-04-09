# Copyright (c) 2025 iiPython

# Modules
import click
from pathlib import Path

# Initialization
@click.command()
@click.option(
    "-s", "--start",
    type = click.Choice(["cabin", "group"],
    case_sensitive = True),
    required = True,
    help = "Application to start"
)
@click.option(
    "-c", "--config",
    type = click.Path(exists = True, dir_okay = False, path_type = Path),
    required = True,
    help = "Path to config file"
)
def camp(start: str, config: Path) -> None:
    """Camp: a decentralized communication system."""

    import uvicorn
    from camp.config import load_config

    match start:
        case "cabin":
            from camp.cabin import app


        case "group":
            from camp.group import app

        case _:

            # Shouldn't be called because of click validation, but it silences
            # based pyright so works for me.
            return exit("-s must be one of 'cabin' or 'group'.")

    app.config = getattr(load_config(config), start)
    uvicorn.run(app)
