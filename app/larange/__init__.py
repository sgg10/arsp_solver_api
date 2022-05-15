from flask import Blueprint

larange = Blueprint("larange", __name__, url_prefix="/api/larange")

from app.larange import routes
