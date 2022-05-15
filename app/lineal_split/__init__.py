from flask import Blueprint

lineal_split = Blueprint("lineal_split", __name__, url_prefix="/api/lineal_split")

from app.lineal_split import routes
