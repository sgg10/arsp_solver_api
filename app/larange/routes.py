from flask import request

from . import larange
from .method import Larange


@larange.route('', methods=['GET', 'POST'])
def larange_method():
    try:
        if request.method == "POST":
            return Larange(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Larange",
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
