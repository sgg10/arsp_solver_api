from flask import request

from . import parcial_lu
from .method import Parcial_LU


@parcial_lu.route('', methods=['GET', 'POST'])
def parcial_lu_method():
    try:
        if request.method == "POST":
            return Parcial_LU(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Parcial LU",
                    "arguments": [
                        "A[REQUIRED]",
                        "b[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 2 required arguments: [A, b, n]"
        }
