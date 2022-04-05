from flask import request

from . import tridiagonal
from .method import Tridiagonal

@tridiagonal.route('', methods=["GET", "POST"])
def tridiagonal_method():
    if request.method == "POST":
        return Tridiagonal(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Tridiagonal",
                "arguments": []
            }
        }
