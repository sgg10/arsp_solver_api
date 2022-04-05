from flask import Blueprint

trisection = Blueprint("trisection", __name__, url_prefix="/api/trisection")

from app.trisection import routes
