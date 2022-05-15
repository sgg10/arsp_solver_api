from flask import Flask
from .nonlinear_equations import nonlinear_equations
from .linear_equations import linear_equations
from .interpolation import interpolation


def create_app():
    app = Flask(__name__)

    app.register_blueprint(nonlinear_equations)
    app.register_blueprint(linear_equations)
    app.register_blueprint(interpolation)

    return app
