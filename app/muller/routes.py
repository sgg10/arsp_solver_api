from flask import request

from . import muller
from .method import Muller

@muller.route('', methods=["GET", "POST"])
def muller_method():
    if request.method == "POST":
        return Muller(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Muller",
                "arguments": []
            }
        }
