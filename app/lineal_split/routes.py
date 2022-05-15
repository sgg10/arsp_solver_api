from flask import request

from . import lineal_split
from .method import LinealSplit


@lineal_split.route('', methods=['GET', 'POST'])
def lineal_split_method():
    try:
        if request.method == "POST":
            return LinealSplit(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Lineal Split",
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
