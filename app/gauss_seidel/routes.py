from flask import request

from . import gauss_seidel
from .method import GaussSeidel


@gauss_seidel.route("", methods=["GET", "POST"])
def gauss_seidel_method():
    try:
        if request.method == "POST":
            return GaussSeidel(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Gauss Seidel",
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
