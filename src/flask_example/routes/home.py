from flask import Blueprint

bp = Blueprint("home", __name__)


@bp.get("/")
def index() -> str:
    return "Hello"
