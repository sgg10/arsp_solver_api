from flask import Blueprint


nonlinear_equations = Blueprint("nonlinear_equations", __name__, url_prefix='/api/nonlinear_equations/')

from app.nonlinear_equations import routes
