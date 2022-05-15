from flask import request

from . import simple_lu
from .method import Simple_LU


@simple_lu.route('', methods=['GET', 'POST'])
def simple_lu_method():
    try:
        if request.method == "POST":
            return Simple_LU(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Newton",
                    "arguments": [
                        "A[REQUIRED]",
                        "b[REQUIRED]",
                        "n[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 3 required arguments: [A, b, n]"
        }
