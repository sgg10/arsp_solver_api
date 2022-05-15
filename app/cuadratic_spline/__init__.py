from flask import Blueprint

cuadratic_spline = Blueprint("cuadratic_spline", __name__, url_prefix="/api/cuadratic_spline")

from app.cuadratic_spline import routes
