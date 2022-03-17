from flask import Blueprint

bisection = Blueprint("bisection", __name__, url_prefix="/api/bisection")

from app.Bisection import routes
