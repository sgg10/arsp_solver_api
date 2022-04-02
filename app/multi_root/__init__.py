from flask import Blueprint

multi_root = Blueprint("multi_root", __name__, url_prefix="/api/multi_root")

from app.multi_root import routes
