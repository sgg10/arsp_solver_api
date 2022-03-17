from flask import Flask

from .incremental_search import incremental_search
from .Bisection import bisection
from .fixed_point import fixed_point


def create_app():
    app = Flask(__name__)

    app.register_blueprint(incremental_search)
    app.register_blueprint(bisection)
    app.register_blueprint(fixed_point)

    return app
