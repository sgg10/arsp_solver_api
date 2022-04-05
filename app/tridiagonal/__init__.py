from flask import Blueprint

tridiagonal = Blueprint("tridiagonal", __name__, url_prefix="/api/tridiagonal")

from app.tridiagonal import routes
