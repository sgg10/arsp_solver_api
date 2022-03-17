from flask import request

from . import bisection
from .method import Bisection


@bisection.route('', methods=['GET', "POST"])
def bisection_method():
    try:
        if request.method == "POST":
            return Bisection(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Bisection",
                    "arguments": [
                        "function[REQUIRED]",
                        "iterations[REQUIRED]",
                        "x0[REQUIRED]",
                        "x1[REQUIRED]",
                        "tolerance[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 5 required arguments: [function, iterations, x0, x1, tolerance]"
        }
