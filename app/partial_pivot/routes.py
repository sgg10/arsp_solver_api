from flask import request

from . import partial_pivot
from .method import PartialPivot

@partial_pivot.route('', methods=["GET", "POST"])
def partial_pivot_method():
    if request.method == "POST":
        return PartialPivot(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Partial Pivot",
                "arguments": [
                    "n[REQUIRED]",
                    "A[REQUIRED]",
                ]
            }
        }
