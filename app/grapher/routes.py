from app.utils.response import method_response
from . import grapher_blueprint
from .grapher import Grapher


@grapher_blueprint.route("graph", methods=['GET', 'POST'])
def grapher_method():
    get_res = {
        "arguments": [
            "function [REQUIRED]",
            "a [OPTIONAL]",
            "b [OPTIONAL]",
            "points [OPTIONAL]"
        ]
    }
    error_res = {
        "method_status": "error",
        "message": "Error in the grapher"
    }
    return method_response(Grapher, get_res, error_res)
