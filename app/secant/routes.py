from flask import request

from . import secant
from .method import Secant


@secant.route('', methods=['GET', 'POST'])
def newton_method():
    try:
        if request.method == "POST":
            return Secant(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Newton",
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
            "message": "Missing 4 required arguments: [function, iterations, x0, tolerance]"
        }
