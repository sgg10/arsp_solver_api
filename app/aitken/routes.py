from flask import request

from . import aitken
from .method import Aitken

@aitken.route('', methods=["GET", "POST"])
def aitken_method():
    if request.method == "POST":
        return Aitken(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Aitken",
                "arguments": []
            }
        }
