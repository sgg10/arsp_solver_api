from flask import request

from . import cholesky
from .method import Cholesky


@cholesky.route('', methods=['GET', 'POST'])
def cholesky_method():
    try:
        if request.method == "POST":
            return Cholesky(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Cholesky",
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
