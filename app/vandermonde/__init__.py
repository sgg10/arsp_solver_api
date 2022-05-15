from flask import Blueprint

vandermonde = Blueprint("vandermonde", __name__, url_prefix='/api/vandermonde')

from app.vandermonde import routes
