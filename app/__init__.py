from flask import Flask

from .incremental_search import incremental_search
from .Bisection import bisection
from .fixed_point import fixed_point
from .false_rule import false_rule
from .Newton import newton
from .secant import secant


def create_app():
    app = Flask(__name__)

    app.register_blueprint(incremental_search)
    app.register_blueprint(bisection)
    app.register_blueprint(fixed_point)
    app.register_blueprint(false_rule)
    app.register_blueprint(newton)
    app.register_blueprint(secant)

    return app
