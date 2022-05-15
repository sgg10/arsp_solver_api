from flask import Blueprint


linear_equations = Blueprint("linear_equations", __name__, url_prefix='/api/linear_equations/')

from app.linear_equations import routes
