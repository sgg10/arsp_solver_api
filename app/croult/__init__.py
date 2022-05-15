from flask import Blueprint

croult = Blueprint("croult", __name__, url_prefix="/api/croult")

from app.croult import routes
