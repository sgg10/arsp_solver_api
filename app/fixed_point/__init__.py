from flask import Blueprint

fixed_point = Blueprint("fixed_point", __name__, url_prefix="/api/fixed_point")

from app.fixed_point import routes
