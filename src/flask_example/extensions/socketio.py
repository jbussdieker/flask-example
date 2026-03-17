from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def init_app(app: Flask) -> None:
    socketio.init_app(app)


__all__ = ["socketio", "init_app"]
