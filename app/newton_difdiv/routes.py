from flask import request

from . import newton_difdiv
from .method import NewtonDifDiv


@newton_difdiv.route('', methods=['GET', 'POST'])
def newton_difdiv_method():
    try:
        if request.method == "POST":
            return NewtonDifDiv(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Newton Dif Div",
                    "arguments": [
                        "n[REQUIRED]",
                        "table[REQUIRED]",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 2 required arguments: [n, table]"
        }
