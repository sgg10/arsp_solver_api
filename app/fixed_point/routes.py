from flask import request

from . import fixed_point
from .method import FixedPoint


@fixed_point.route("", methods=['GET', 'POST'])
def fixed_point_method():
    try:
        if request.method == "POST":
            return FixedPoint(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Fixed Point",
                    "arguments": [
                        "f[REQUIRED]",
                        "g[REQUIRED]",
                        "xa[REQUIRED]",
                        "iterations[REQUIRED]",
                        "tolerance[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 5 required arguments: [f, g, xa, iterations, tolerance]"
        }
