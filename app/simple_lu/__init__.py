from flask import Blueprint

simple_lu = Blueprint("simple_lu", __name__, url_prefix="/api/simple_lu")

from app.simple_lu import routes
