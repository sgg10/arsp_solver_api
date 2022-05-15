from flask import request

from . import lineal_spline
from .method import LinealSpline


@lineal_spline.route('', methods=['GET', 'POST'])
def lineal_spline_method():
    try:
        if request.method == "POST":
            return LinealSpline(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Lineal Spline",
                    "arguments": [
                        "n[REQUIRED]",
                        "x[REQUIRED]",
                        "y[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 2 required arguments: [n, x, y]"
        }
