from app.utils.response import method_response
from . import linear_equations
from .elimination import GaussianElimination, PartialPivot, TotalPivot
from .factorization import SimpleLU, PartialLU, Croult, Doolittle, Cholesky
from .iterative import Jacobi, GaussSeidel, SOR, Vandermonde


# Elimination methods
@linear_equations.route("elimination/gaussian_elimination", methods=['GET', 'POST'])
def gaussian_elimination_method():
    get_res = {
        "method": {
            "name": "Gaussian Elimination",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [A, b]"
    }
    return method_response(GaussianElimination, get_res, error_res)


@linear_equations.route("elimination/partial_pivot", methods=['GET', 'POST'])
def partial_pivot_method():
    get_res = {
        "method": {
            "name": "Partial Pivot",
            "arguments": [
                "n[REQUIRED]",
                "A[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [A, n]"
    }
    return method_response(PartialPivot, get_res, error_res)


@linear_equations.route("elimination/total_pivot", methods=['GET', 'POST'])
def total_pivot_method():
    get_res = {
        "method": {
            "name": "Total Pivot",
            "arguments": [
                "n[REQUIRED]",
                "A[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 2 required arguments: [A, n]"
    }
    return method_response(TotalPivot, get_res, error_res)


# Factorization methods
@linear_equations.route("factorization/simple_lu", methods=['GET', 'POST'])
def simple_lu_method():
    get_res = {
        "method": {
            "name": "Simple LU",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "n[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [A, b, n]"
    }
    return method_response(SimpleLU, get_res, error_res)


@linear_equations.route("factorization/partial_lu", methods=['GET', 'POST'])
def partial_lu_method():
    get_res = {
        "method": {
            "name": "Partial LU",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "n[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [A, b, n]"
    }
    return method_response(PartialLU, get_res, error_res)


@linear_equations.route("factorization/croult", methods=['GET', 'POST'])
def croult_method():
    get_res = {
        "method": {
            "name": "Croult",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "n[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [A, b, n]"
    }
    return method_response(Croult, get_res, error_res)


@linear_equations.route("factorization/doolittle", methods=['GET', 'POST'])
def doolittle_method():
    get_res = {
        "method": {
            "name": "Croult",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "n[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [A, b, n]"
    }
    return method_response(Doolittle, get_res, error_res)


@linear_equations.route("factorization/cholesky", methods=['GET', 'POST'])
def cholesky_method():
    get_res = {
        "method": {
            "name": "Cholesky",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "n[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 3 required arguments: [A, b, n]"
    }
    return method_response(Cholesky, get_res, error_res)


# Iterative methods
@linear_equations.route("iterative/jacobi", methods=['GET', 'POST'])
def jacobi_method():
    get_res = {
        "method": {
            "name": "Jacobi",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "x0[REQUIRED]",
                "n[REQUIRED]",
                "iterations[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 6 required arguments: [A, b, x0, n, iterations, tolerance]"
    }
    return method_response(Jacobi, get_res, error_res)


@linear_equations.route("iterative/gauss_seidel", methods=['GET', 'POST'])
def gauss_seidel_method():
    get_res = {
        "method": {
            "name": "Gauss Seidel",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "x0[REQUIRED]",
                "n[REQUIRED]",
                "iterations[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 6 required arguments: [A, b, x0, n, iterations, tolerance]"
    }
    return method_response(GaussSeidel, get_res, error_res)


@linear_equations.route("iterative/sor", methods=['GET', 'POST'])
def sor_method():
    get_res = {
        "method": {
            "name": "SOR",
            "arguments": [
                "A[REQUIRED]",
                "b[REQUIRED]",
                "omega[REQUIRED]",
                "x0[REQUIRED]",
                "n[REQUIRED]",
                "iterations[REQUIRED]",
                "tolerance[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 7 required arguments: [A, b, omega, x0, n, iterations, tolerance]"
    }
    return method_response(SOR, get_res, error_res)


@linear_equations.route("iterative/vandermonde", methods=['GET', 'POST'])
def vandermonde_method():
    get_res = {
        "method": {
            "name": "Vandermonde",
            "arguments": [
                "x[REQUIRED]",
            ]
        }
    }
    error_res = {
        "method_status": "error",
        "message": "Missing 1 required arguments: x"
    }
    return method_response(Vandermonde, get_res, error_res)
