from flask import Blueprint


grapher_blueprint = Blueprint("grapher", __name__, url_prefix='/api/grapher/')

from app.grapher import routes
