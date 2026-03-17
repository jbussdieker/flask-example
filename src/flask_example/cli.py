import click
from flask.cli import FlaskGroup

from .factory import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def main() -> None:
    """Flask Example"""
