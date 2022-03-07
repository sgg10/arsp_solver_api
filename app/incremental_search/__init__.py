from flask import Blueprint

incremental_search = Blueprint(
    "incremental_search", __name__, url_prefix='/api/incremental_search')

from . import routes
