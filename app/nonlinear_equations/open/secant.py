from app.utils.methods import BaseMethod
from sympy import Function, Symbol
from sympy.parsing.sympy_parser import parse_expr


class Secant(BaseMethod):
    f = Function('fx')

    def __init__(self, x0, x1, tolerance, iterations, function):
        self.x0 = float(x0)
        self.x1 = float(x1)
        self.tol = tolerance
        self.iter = iterations
        self.function = function
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol('x')
        fx0 = f.subs(x, self.x0)

        if fx0 == 0:
            return {
                "method_status": "success",
                "result": f"{self.x0} is a root",
            }
        else:
            fx1 = f.subs(x, self.x1)
            error = self.tol + 1
            denominator = self.x1 - self.x0
            self.array.append(["0", str(self.x0), str(fx0), "0"])
            for i in range(1, self.iter):
                if fx1 == 0 or error <= self.tol or denominator == 0:
                    break
                fp = (fx1 - fx0) / denominator
                x2 = self.x1 - fx1 / fp
                error = abs(x2 - self.x1)
                rel_error = error / x2
                self.x0 = self.x1
                self.x1 = x2
                fx0 = f.subs(x, self.x0)
                fx1 = f.subs(x, self.x1)
                denominator = self.x1 - self.x0
                self.array.append([str(i), str(self.x0), str(fx0), str(rel_error)])

            if fx1 == 0:
                return {
                    "method_status": "success",
                    "result": f"{self.x1} is a root",
                    "iterations": self.array
                }
            elif error < self.tol:
                return {
                    "method_status": "success",
                    "result": f"{self.x0} approaches a root of the function with a tolerance of {self.tol}",
                    "iterations": self.array
                }
            elif denominator == 0:
                return {
                    "method_status": "success",
                    "result": f"There is a multiple root in {self.x1}",
                    "iterations": self.array
                }
            else:
                return {
                    "method_status": "failed",
                    "result": "Max interactions exceeded",
                    "iterations": self.array
                }
