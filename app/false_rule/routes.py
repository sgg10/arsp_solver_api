from flask import request

from . import false_rule
from .method import FalseRule


@false_rule.route('', methods=['GET', 'POST'])
def false_rule_method():
    # try:
    if request.method == "POST":
        return FalseRule(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "False Rule",
                "arguments": [
                    "function[REQUIRED]",
                    "iterations[REQUIRED]",
                    "x0[REQUIRED]",
                    "x1[REQUIRED]",
                    "tolerance[REQUIRED]",
                ]
            }
        }
    """except:
        return {
            "method_status": "error",
            "message": "Missing 5 required arguments: [function, iterations, x0, x1, tolerance]"
        }"""
