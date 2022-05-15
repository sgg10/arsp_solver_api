from flask import request

from . import vandermonde
from .method import Vandermonde


@vandermonde.route("", methods=["GET", "POST"])
def vandermonde_method():
    try:
        if request.method == "POST":
            return Vandermonde(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Vandermonde",
                    "arguments": [
                        "x[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 1 required arguments: x"
        }
