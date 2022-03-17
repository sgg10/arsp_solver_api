from flask import request

from . import bisection
from .method import Bisection

@bisection.route('', methods=['GET', "POST"])
def bisection_method():
    if request.method == "POST":
        result = Bisection(**request.get_json()).run()
        print(result)
        return result
    else:
        return {
            "method": {
                "name": "Bisection",
                "arguments": [
                    "function[REQUIRED]",
                    "iterations[REQUIRED]",
                    "x0[REQUIRED]",
                    "x1[REQUIRED]"
                    "tolerance[REQUIRED] -> if you pass a x1",
                ]
            }
        }