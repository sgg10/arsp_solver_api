from app.utils.methods import BaseMethod
from sympy import Function, Symbol
from sympy.parsing.sympy_parser import parse_expr


class Bisection(BaseMethod):
    f = Function("fX")

    def __init__(self, x0, x1, tolerance, iterations, function, **kwargs):
        self.xl = x0
        self.xh = x1
        self.tol = tolerance
        self.iter = iterations
        self.function = function
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol("x")
        fxl = f.subs(x, self.xl)
        fxh = f.subs(x, self.xh)

        if fxl == 0:
            return {
                "method_status": "success",
                "result": f"{self.xl} is a root",
            }
        elif fxh == 0:
            return {
                "method_status": "success",
                "result": f"{self.xh} is a root",
                "iterations": self.array
            }
        elif fxl * fxh > 0:
            return {
                "method_status": "failed",
                "result": "The interval does not have a root"
            }
        else:
            error = self.tol + 1
            xm = (self.xl + self.xh) / 2
            for i in range(self.iter):
                fxm = f.subs(x, xm)

                if fxm == 0 or error <= self.tol or i >= self.iter:
                    break

                if fxl * fxh < 0:
                    self.xh = xm
                    fxh = f.subs(x, self.xh)
                    # self.array.append([str(i), str(self.xl), str(xm), str(self.xh), str(fxm), str(error)])
                else:
                    self.xl = xm
                    fxl = f.subs(x, self.xl)

                x_aux = xm
                xm = (self.xl + self.xh) / 2
                error = abs(xm - x_aux)
                self.array.append([str(i), str(self.xl), str(xm), str(self.xh), str(fxm), str(error)])

            print(self.array)

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
