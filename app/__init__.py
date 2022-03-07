from flask import Flask

from .incremental_search import incremental_search


def create_app():
    app = Flask(__name__)

    app.register_blueprint(incremental_search)

    return app
