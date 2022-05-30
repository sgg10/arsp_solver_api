from app.utils.methods import BaseMethod
from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr


class Bisection(BaseMethod):

    def __init__(self, x0, x1, tolerance, iterations, function, **kwargs):
        self.xl = float(x0)
        self.xh = float(x1)
        self.tol = float(tolerance)
        self.iter = int(iterations)
        self.function = function
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol("x")
        fxl = f.subs(x, self.xl)
        fxh = f.subs(x, self.xh)

        if fxl == 0:
            return self.success_response(f"{self.xl} is a root")
        elif fxh == 0:
            return self.success_response(f"{self.xh} is a root")
        elif fxl * fxh > 0:
            return self.failed_response("The interval does not have a root")
        else:
            error = self.tol + 1
            xm = (self.xl + self.xh) / 2
            self.array.append(["i", "x0", "x1", "xm", "f(xm)", "error"])
            for i in range(self.iter):
                fxm = f.subs(x, xm)

                if fxm == 0 or error <= self.tol:
                    break

                if fxl * fxm < 0:
                    self.xh = xm
                else:
                    self.xl = xm

                x_aux = xm
                xm = (self.xl + self.xh) / 2
                error = abs(xm - x_aux)
                self.array.append([str(i), str(self.xl), str(xm), str(self.xh), str(fxm), str(error)])

            if fxm == 0:
                return {
                    "method_status": "success",
                    "result": f"{xm} is a root",
                    "iterations": self.array
                }
            elif error < self.tol:
                return {
                    "method_status": "success",
                    "result": f"{xm} approaches a root of the function with a tolerance of {self.tol}",
                    "iterations": self.array
                }
            else:
                return {
                    "method_status": "failed",
                    "result": "Max interactions exceeded",
                    "iterations": self.array
                }
