from app.utils.methods import BaseMethod
from sympy import Function, Symbol
from sympy.parsing.sympy_parser import parse_expr


class FalseRule(BaseMethod):
    f = Function("fx")

    def __init__(self, x0, x1, function, tolerance, iterations, **kwargs):
        self.xl = float(x0)
        self.xh = float(x1)
        self.function = function
        self.tol = tolerance
        self.iter = int(iterations)
        self.array = []

    def run(self):
        f = parse_expr(self.function)
        x = Symbol('x')
        fxl = f.subs(x, self.xl)
        fxh = f.subs(x, self.xh)

        if fxl == 0:
            return {
                "method_status": "success",
                "result": f"{fxl} is a root"
            }
        elif fxh == 0:
            return {
                "method_status": "success",
                "result": f"{fxh} is a root"
            }
        elif fxl * fxh < 0:
            xm = self.xl - ((fxl * (self.xl - self.xh)) / (fxl - fxh))
            error = self.tol + 1
            self.array.append(["i", "x0", "x1", "xm", "f(xm)", "error"])
            for i in range(self.iter):
                fxm = f.subs(x, xm)
                if fxm == 0 or error <= self.tol:
                    break

                if fxl * fxm < 0:
                    self.xh = xm
                    fxh = f.subs(x, self.xh)
                else:
                    self.xl = xm
                    fxl = f.subs(x, self.xl)

                x_aux = xm
                xm = self.xl - ((fxl * (self.xl - self.xh)) / (fxl - fxh))
                error = abs(xm - x_aux)
                self.array.append([str(i), str(self.xl), str(xm), str(self.xl), str(fxm), str(error)])

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

        else:
            return {
                "method_status": "failed",
                "result": f"The interval does not meet the conditions to search for a root"
            }
