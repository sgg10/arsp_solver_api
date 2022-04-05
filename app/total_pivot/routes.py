from flask import request

from . import total_pivot
from .method import TotalPivot

@total_pivot.route('', methods=["GET", "POST"])
def total_pivot_method():
    if request.method == "POST":
        return TotalPivot(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Total Pivot",
                "arguments": [
                    "n[REQUIRED]",
                    "A[REQUIRED]",
                ]
            }
        }
