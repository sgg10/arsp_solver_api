from flask import Blueprint


interpolation = Blueprint('interpolation', __name__, url_prefix='/api/interpolation/')

from app.interpolation import routes
