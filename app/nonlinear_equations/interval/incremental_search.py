from sympy import Function, Symbol
from sympy.parsing.sympy_parser import parse_expr
from app.utils.methods import BaseMethod
from app.grapher.grapher import Grapher


class IncrementalSearch(BaseMethod):
    f = Function("fx")

    def __init__(self, function, iterations, x0, x1=None, delta=None, **kwargs):
        self.error = None
        if not x1 and not delta:
            self.error = "You must specify a delta or x1 parameter"
        else:
            if x1:
                delta = abs(float(x1) - float(x0))
            self.x1 = x1
            self.x0 = float(x0)
            self.delta = float(delta)
            self.iterations = int(iterations)
            self.function = function

    def run(self):
        if self.error:
            return {
                "method_status": "failed",
                "result": self.error
            }
        f = parse_expr(self.function)
        x = Symbol("x")
        fx0 = f.subs(x, self.x0)
        roots = []
        if fx0 == 0:
            roots.append(f'{self.x0} is a root')
        else:
            for _ in range(self.iterations):
                x1 = self.x0 + self.delta
                fx1 = f.subs(x, x1)

                if fx0 * fx1 < 0:
                    roots.append(f"root between {self.x0} and {x1}")
                    break
                if fx1 == 0:
                    roots.append(f'{x1} is a root')
                    break

                self.x0 = x1
                fx0 = fx1

        if roots:
            return {
                "method_status": "success",
                "result": roots
            }
        else:
            return {
                "method_status": "failed",
                "result": "Max interactions exceeded"
            }
