from flask import Blueprint

cubic_spline = Blueprint("cubic_spline", __name__, url_prefix="/api/cubic_spline")

from app.cubic_spline import routes
