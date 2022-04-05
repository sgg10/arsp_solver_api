from flask import Blueprint

gaussian_elimination = Blueprint("gaussian_elimination", __name__, url_prefix="/api/gaussian_elimination")

from app.gaussian_elimination import routes
