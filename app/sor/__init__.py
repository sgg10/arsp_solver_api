from flask import Blueprint

sor = Blueprint("sor", __name__, url_prefix='/api/sor')

from app.sor import routes
