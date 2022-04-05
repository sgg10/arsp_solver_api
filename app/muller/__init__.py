from flask import Blueprint

muller = Blueprint("muller", __name__, url_prefix="/api/muller")

from app.muller import routes
