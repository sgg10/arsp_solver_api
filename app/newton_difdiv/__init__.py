from flask import Blueprint

newton_difdiv = Blueprint("newton_difdiv", __name__, url_prefix="/api/newton_difdiv")

from app.newton_difdiv import routes
