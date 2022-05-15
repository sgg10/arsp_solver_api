from app.utils.response import method_response
from . import interpolation
from .methods import NewtonDifDiv, Larange, LinearSpline, QuadraticSpline, CubicSpline


@interpolation.route('divided_differences', methods=['GET', 'POST'])
def divided_differences_method():
    get_res = {
        "method": {
            "name": "Newton Divided Differences",
            "arguments": [
                "n[REQUIRED]",
                "table[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [n, table]"
    }
    return method_response(NewtonDifDiv, get_res, error_res)


@interpolation.route('larange', methods=['GET', 'POST'])
def larange_method():
    get_res = {
        "method": {
            "name": "Larange",
            "arguments": [
                "n[REQUIRED]",
                "x[REQUIRED]",
                "y[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [n, x, y]"
    }
    return method_response(Larange, get_res, error_res)


@interpolation.route('linear_spline', methods=['GET', 'POST'])
def linear_spline_method():
    get_res = {
        "method": {
            "name": "Linear Spline",
            "arguments": [
                "n[REQUIRED]",
                "x[REQUIRED]",
                "y[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [n, x, y]"
    }
    return method_response(LinearSpline, get_res, error_res)


@interpolation.route('quadratic_spline', methods=['GET', 'POST'])
def quadratic_spline_method():
    get_res = {
        "method": {
            "name": "Quadratic Spline",
            "arguments": [
                "x[REQUIRED]",
                "y[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [x, y]"
    }
    return method_response(QuadraticSpline, get_res, error_res)


@interpolation.route('cubic_spline', methods=['GET', 'POST'])
def cubic_spline_method():
    get_res = {
        "method": {
            "name": "Cubic Spline",
            "arguments": [
                "x[REQUIRED]",
                "y[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [x, y]"
    }
    return method_response(CubicSpline, get_res, error_res)
