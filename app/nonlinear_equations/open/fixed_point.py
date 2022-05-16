from app.utils.methods import BaseMethod
from sympy import Function, Symbol
from sympy.parsing.sympy_parser import parse_expr


class FixedPoint(BaseMethod):

    f = Function("fx")
    g = Function("gx")

    def __init__(self, xa, tolerance, iterations, f, g, **kwargs):
        self.xa = float(xa)
        self.tol = tolerance
        self.iter = int(iterations)
        self.f = f
        self.g = g
        self.array = []

    def run(self):
        f = parse_expr(self.f)
        g = parse_expr(self.g)
        x = Symbol('x')
        fx = f.subs(x, self.xa)
        error = self.tol + 1
        self.array.append(["0", str(self.xa), str(fx), str(error)])
        for i in range(self.iter):
            if fx == 0 or error <= self.tol:
                break

            xn = float(g.subs(x, self.xa))
            fx = f.subs(x, xn)
            error = abs(xn - self.xa)
            self.xa = xn

            self.array.append([str(i), str(xn), str(fx), str(error)])

        if fx == 0:
            return {
                "method_status": "success",
                "result": f'{self.xa} is a root',
                "iterations": self.array
            }
        elif error < self.tol:
            return {
                "method_status": "success",
                "result": f'{self.xa} approaches a root of the function with a tolerance of {self.tol}',
                "iterations": self.array
            }
        else:
            return {
                "method_status": "failed",
                "result": "Max interactions exceeded",
                "iterations": self.array
            }

