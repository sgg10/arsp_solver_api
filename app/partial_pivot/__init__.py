from flask import Blueprint

partial_pivot = Blueprint("partial_pivot", __name__, url_prefix="/api/partial_pivot")

from app.partial_pivot import routes
