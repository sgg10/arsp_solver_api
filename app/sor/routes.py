from flask import request

from . import sor
from .method import SOR


@sor.route("", methods=["GET", "POST"])
def sor_method():
    try:
        if request.method == "POST":
            return SOR(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "SOR",
                    "arguments": [
                        "A[REQUIRED]",
                        "b[REQUIRED]",
                        "omega[REQUIRED]",
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
            "message": "Missing 7 required arguments: [A, b, omega, x0, n, iterations, tolerance]"
        }
