from flask import Blueprint

gauss_seidel = Blueprint("gauss_seidel", __name__, url_prefix='/api/gauss_seidel')

from app.gauss_seidel import routes
