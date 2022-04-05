from flask import Blueprint

aitken = Blueprint("aitken", __name__, url_prefix="/api/aitken")

from app.aitken import routes
