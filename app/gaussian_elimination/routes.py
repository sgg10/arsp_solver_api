from flask import request

from . import gaussian_elimination
from .method import GaussianElimination

@gaussian_elimination.route('', methods=["GET", "POST"])
def gaussian_elimination_method():
    if request.method == "POST":
        return GaussianElimination(**request.get_json()).run()
    else:
        return {
            "method": {
                "name": "Gaussian Elimination",
                "arguments": [
                    "n[REQUIRED]",
                    "A[REQUIRED]",
                ]
            }
        }
