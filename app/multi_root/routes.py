from flask import request

from . import multi_root
from .method import MultiRoot

@multi_root.route('', methods=["GET", "POST"])
def multi_root_method():
    if request.method == "POST":
        return MultiRoot(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Newton",
                "arguments": [
                    "x0[REQUIRED]",
                    "function[REQUIRED]",
                    "iterations[REQUIRED]",
                    "tolerance[REQUIRED]",
                ]
            }
        }