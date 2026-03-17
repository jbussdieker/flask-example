from typing import Protocol, runtime_checkable, Iterable, Any
from importlib.metadata import entry_points
from importlib import resources
import click
from flask import Flask, Blueprint


@runtime_checkable
class FlaskExtension(Protocol):
    def __call__(self, app: Flask) -> None: ...


def _load(group: str) -> Iterable[Any]:
    for ep in entry_points().select(group=group):
        try:
            yield ep.load()
        except Exception as e:
            print(f"Plugin load failure: {ep.name}: {e}")


def load_blueprints(app: Flask) -> None:
    for obj in _load("flask_example.blueprints"):
        if isinstance(obj, Blueprint):
            app.register_blueprint(obj)


def load_extensions(app: Flask) -> None:
    for obj in _load("flask_example.extensions"):
        if isinstance(obj, FlaskExtension):
            obj(app)


def load_cli(app: Flask) -> None:
    for obj in _load("flask_example.cli"):
        if isinstance(obj, click.Command):
            app.cli.add_command(obj)


def load_templates(app: Flask) -> None:
    loader = app.jinja_loader
    if loader is None or not hasattr(loader, "searchpath"):
        return

    for pkg in _load("flask_example.templates"):
        template_path = resources.files(pkg) / "templates"
        loader.searchpath.append(str(template_path))
