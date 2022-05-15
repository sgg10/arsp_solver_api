from flask import Blueprint

parcial_lu = Blueprint("parcial_lu", __name__, url_prefix="/api/parcial_lu")

from app.parcial_lu import routes
