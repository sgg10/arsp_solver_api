from flask import Blueprint

secant = Blueprint("secant", __name__, url_prefix="/api/secant")

from app.secant import routes
