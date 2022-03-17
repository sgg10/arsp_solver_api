from flask import Blueprint

false_rule = Blueprint("false_rule", __name__, url_prefix="/api/false_rule")

from app.false_rule import routes