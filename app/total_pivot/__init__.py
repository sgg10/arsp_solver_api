from flask import Blueprint

total_pivot = Blueprint("total_pivot", __name__, url_prefix="/api/total_pivot")

from app.total_pivot import routes
