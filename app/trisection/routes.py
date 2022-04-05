from flask import request

from . import trisection
from .method import Trisection

@trisection.route('', methods=["GET", "POST"])
def trisection_method():
    if request.method == "POST":
        return Trisection(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Trisection",
                "arguments": []
            }
        }
