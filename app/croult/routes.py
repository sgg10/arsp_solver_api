from flask import request

from . import croult
from .method import Croult


@croult.route('', methods=['GET', 'POST'])
def false_rule_method():
    try:
        if request.method == "POST":
            return Croult(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Croult",
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
