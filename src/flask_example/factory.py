from flask import Flask

from .config import Config
from .plugins import (
    load_extensions,
    load_templates,
    load_blueprints,
    load_cli,
)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    load_extensions(app)
    load_templates(app)
    load_blueprints(app)
    load_cli(app)

    return app
