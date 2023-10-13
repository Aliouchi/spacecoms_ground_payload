"""Running Flask Server"""

from __future__ import annotations

from flask import Flask


def create_app():
    app = Flask(__name__)

    return app
