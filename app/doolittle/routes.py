from flask import request

from . import doolittle
from .method import Doolittle


@doolittle.route('', methods=['GET', 'POST'])
def doolittle_method():
    try:
        if request.method == "POST":
            return Doolittle(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Doolittle",
                    "arguments": [
                        "A[REQUIRED]",
                        "B[REQUIRED]",
                        "n[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 3 required arguments: [A, B, n]"
        }
