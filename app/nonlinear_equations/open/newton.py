from app.utils.methods import BaseMethod
from sympy import Function, Symbol, diff
from sympy.parsing.sympy_parser import parse_expr


class Newton(BaseMethod):
    f = Function("fx")
    df = Function("dfx")

    def __init__(self, function, x0, tolerance, iterations):
        self.function = function
        self.x0 = x0
        self.tol = tolerance
        self.iterations = int(iterations)
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol("x")
        df = diff(f, x)
        fx = f.subs(x, self.x0)
        dfx = f.subs(x, self.x0)
        error = self.tol + 1
        self.array.append(["0", str(self.x0), str(fx), str(dfx), "0"])
        for i in range(1, self.iterations):
            if fx == 0 or error <= self.tol or dfx == 0:
                break

            x1 = self.x0 - (fx / dfx)
            fx = f.subs(x, x1)
            dfx = df.subs(x, x1)
            error = abs(x1 - self.x0)
            rel_error = error / x1
            self.x0 = x1

            self.array.append([str(i), str(self.x0), str(fx), str(dfx), str(rel_error)])

        if fx == 0:
            return {
                "method_status": "success",
                "result": f"{self.x0} is a root",
                "iterations": self.array
            }
        elif error < self.tol:
            return {
                "method_status": "success",
                "result": f"{self.x0} approaches a root of the function with a tolerance of {self.tol}",
                "iterations": self.array
            }
        elif dfx == 0:
            return {
                "method_status": "success",
                "result": f"{self.x0} is a possible multiple root",
                "iterations": self.array
            }
        else:
            return {
                "method_status": "failed",
                "result": "Max interactions exceeded",
                "iterations": self.array
            }
