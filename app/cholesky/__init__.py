from flask import Blueprint

cholesky = Blueprint("cholesky", __name__, url_prefix="/api/cholesky")

from app.cholesky import routes
