from flask import Blueprint

doolittle = Blueprint("doolittle", __name__, url_prefix="/api/doolittle")

from app.doolittle import routes
