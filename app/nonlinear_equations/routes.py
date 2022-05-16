from app.utils.response import method_response
from . import nonlinear_equations
from .interval import IncrementalSearch, Bisection, FalseRule
from .open import FixedPoint, Newton, Secant, MultiRoot


# Interval methods
@nonlinear_equations.route('interval/incremental_search', methods=['GET', 'POST'])
def incremental_search_method():
    get_res = {
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
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [function, iterations, x0]"
    }
    return method_response(IncrementalSearch, get_res, error_res)


@nonlinear_equations.route('interval/bisection', methods=['GET', 'POST'])
def bisection_method():
    get_res = {
        "method": {
            "name": "Bisection",
            "arguments": [
                "function[REQUIRED]",
                "iterations[REQUIRED]",
                "x0[REQUIRED]",
                "x1[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 5 required arguments: [function, iterations, x0, x1, tolerance]"
    }
    return method_response(Bisection, get_res, error_res)


@nonlinear_equations.route('interval/false_rule', methods=['GET', 'POST'])
def false_rule_method():
    get_res = {
        "method": {
            "name": "False Rule",
            "arguments": [
                "function[REQUIRED]",
                "iterations[REQUIRED]",
                "x0[REQUIRED]",
                "x1[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 5 required arguments: [function, iterations, x0, x1, tolerance]"
    }
    return method_response(FalseRule, get_res, error_res)


# Open methods
@nonlinear_equations.route('open/fixed_point', methods=['GET', 'POST'])
def fixed_point_method():
    get_res = {
        "method": {
            "name": "Fixed Point",
            "arguments": [
                "f[REQUIRED]",
                "g[REQUIRED]",
                "xa[REQUIRED]",
                "iterations[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 5 required arguments: [f, g, xa, iterations, tolerance]"
    }
    return method_response(FixedPoint, get_res, error_res)


@nonlinear_equations.route('open/newton', methods=['GET', 'POST'])
def newton_method():
    get_res = {
        "method": {
            "name": "Newton",
            "arguments": [
                "function[REQUIRED]",
                "iterations[REQUIRED]",
                "x0[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 4 required arguments: [function, iterations, x0, tolerance]"
    }
    return method_response(Newton, get_res, error_res)


@nonlinear_equations.route('open/secant', methods=['GET', 'POST'])
def secant_method():
    get_res = {
        "method": {
            "name": "Secant",
            "arguments": [
                "function[REQUIRED]",
                "iterations[REQUIRED]",
                "x0[REQUIRED]",
                "x1[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 5 required arguments: [function, iterations, x0, x1, tolerance]"
    }
    return method_response(Secant, get_res, error_res)


@nonlinear_equations.route('open/multi_root', methods=['GET', 'POST'])
def multi_root_method():
    get_res = {
        "method": {
            "name": "Multi Root",
            "arguments": [
                "function[REQUIRED]",
                "iterations[REQUIRED]",
                "x0[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 4 required arguments: [function, iterations, x0, tolerance]"
    }
    return method_response(MultiRoot, get_res, error_res)
