import io
import base64
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Qt5agg')
from sympy import Function, Symbol, diff, integrate
from sympy.parsing.sympy_parser import parse_expr


class Grapher:

    def __init__(self, function, a=-10, b=10, points=100, **kwargs):
        self.f = parse_expr(function)
        self.x = Symbol("x")
        self.a = float(a)
        self.b = float(b)
        self.points = int(points)

    @staticmethod
    def convert_graph_to_b64(fig):
        graph_string = io.BytesIO()
        fig.savefig(graph_string, format="jpg")
        graph_string.seek(0)
        return base64.b64encode(graph_string.read())

    def get_diffs(self):
        return diff(self.f, self.x).simplify()

    def run(self):
        x = np.linspace(self.a, self.b, self.points)
        y = [self.f.subs(self.x, _x) for _x in x]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(title=f"{self.f}")
        ax.grid()

        result = {
            "graph_image": self.convert_graph_to_b64(fig).decode(),
            "derivative_function": str(diff(self.f, self.x).simplify()),
            "integrate_function": str(integrate(self.f, self.x).simplify())
        }

        _simplify = str(self.f.simplify())
        result["simplified_function"] = _simplify if str(self.f) != _simplify else ''

        return result


if __name__ == "__main__":
    f = "x**2 - x**3 + x + x + 1"
    G = Grapher(f)
    print(G.run())
