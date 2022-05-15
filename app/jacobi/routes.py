from flask import request

from . import jacobi
from .method import Jacobi


@jacobi.route("", methods=["GET", "POST"])
def jacobi_method():
    try:
        if request.method == "POST":
            return Jacobi(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Jacobi",
                    "arguments": [
                        "A[REQUIRED]",
                        "b[REQUIRED]",
                        "x0[REQUIRED]",
                        "n[REQUIRED]",
                        "iterations[REQUIRED]",
                        "tolerance[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 6 required arguments: [A, b, x0, n, iterations, tolerance]"
        }
