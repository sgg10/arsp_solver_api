from flask import Flask
from flask_cors import CORS
from .nonlinear_equations import nonlinear_equations
from .linear_equations import linear_equations
from .interpolation import interpolation
from .grapher import grapher_blueprint


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resource={r"/api/*": {"origins": "*"}})

    app.register_blueprint(nonlinear_equations)
    app.register_blueprint(linear_equations)
    app.register_blueprint(interpolation)
    app.register_blueprint(grapher_blueprint)

    return app
