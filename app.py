"""Running Flask Server"""

from __future__ import annotations

from flask import Flask


def create_app():
    """A function creating and starting an app on the flask server"""
    app = Flask(__name__)

    return app
