from app.utils.methods import BaseMethod
from sympy import Symbol, Function, diff
from sympy.parsing.sympy_parser import parse_expr


class MultiRoot(BaseMethod):

    def __init__(self, x0, function, tolerance, iterations):
        self.x0 = float(x0)
        self.tol = float(tolerance)
        self.iter = int(iterations)
        self.function = function
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol('x')
        df = diff(f, x)
        d2f = diff(df, x)

        fx = f.subs(x, self.x0)
        dfx = df.subs(x, self.x0)
        d2fx = d2f.subs(x, self.x0)

        error = self.tol + 1
        denominator = dfx ** 2 - (fx * d2fx)
        self.array.append(['0', str(self.x0), str(fx), str(dfx), str(d2fx), str(error)])

        for i in range(1, self.iter):
            if fx == 0 or error <= self.tol or denominator == 0:
                break

            x1 = self.x0 - (fx * dfx) / denominator
            fx = f.subs(x, x1)
            dfx = df.subs(x, x1)
            d2fx = d2f.subs(x, x1)

            error = abs(x1 - self.x0)
            self.x0 = x1
            denominator = dfx ** 2 - (fx * d2fx)
            self.array.append([str(i), str(self.x0), str(fx), str(dfx), str(d2fx), str(error)])

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
                "result": f"{self.x0} is a simple multiple root",
                "iterations": self.array
            }
        elif d2fx == 0:
            return {
                "method_status": "success",
                "result": f"{self.x0} is a multiple root of multiplicity 2",
                "iterations": self.array
            }
        else:
            return {
                "method_status": "failed",
                "result": "Max interactions exceeded",
                "iterations": self.array
            }
