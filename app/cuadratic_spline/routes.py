from flask import request

from . import cuadratic_spline
from .method import run


@cuadratic_spline.route('', methods=['GET', 'POST'])
def cuadratic_spline_method():
    try:
        if request.method == "POST":
            return run(**request.get_json())
        else:
            return {
                "method": {
                    "name": "Cuadratic Spline",
                    "arguments": [
                        "x[REQUIRED]",
                        "y[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 2 required arguments: [x, y]"
        }
