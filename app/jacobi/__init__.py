from flask import Blueprint

jacobi = Blueprint("jacobi", __name__, url_prefix='/api/jacobi')

from app.jacobi import routes
