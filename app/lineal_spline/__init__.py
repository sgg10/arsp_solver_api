from flask import Blueprint

lineal_spline = Blueprint("lineal_spline", __name__, url_prefix="/api/lineal_spline")

from app.lineal_spline import routes
