from flask import request

from . import incremental_search
from .method import IncrementalSearch


@incremental_search.route("", methods=["GET", "POST"])
def incremental_search_method():
    try:
        if request.method == "POST":
            return IncrementalSearch(**request.get_json()).run()
        else:
            return {
                "method": {
                    "name": "Incremental search",
                    "arguments": [
                        "function[REQUIRED]",
                        "iterations[REQUIRED]",
                        "x0[REQUIRED]",
                        "x1[OPTIONAL] -> if you pass delta"
                        "delta[OPTIONAL] -> if you pass a x1",
                    ]
                }
            }
    except:
        return {
            "method_status": "error",
            "message": "Missing 3 required arguments: [function, iterations, x0]"
        }
