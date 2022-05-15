from flask import request

from . import cubic_spline
from .method import run


@cubic_spline.route('', methods=['GET', 'POST'])
def cubic_spline_method():
    try:
        if request.method == "POST":
            return run(**request.get_json())
        else:
            return {
                "method": {
                    "name": "Cubic Spline",
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
