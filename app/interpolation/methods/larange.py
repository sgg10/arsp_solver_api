#from app.utils.methods import BaseMethod
from sympy import expand, Function, symbols, simplify
from sympy.parsing.sympy_parser import parse_expr
import numpy as np


class Larange():
    def __init__(self, x, y, **keywords):

        self.x = np.array(x)
        self.y = np.array(y)
        self.proceso = []

    def lagrange(self, x, y):
        """Interpolates a value using the 'Lagrange polynomial'.
        Args:
            x: an array containing x values.
            y: an array containing y values.
            x_int: value to interpolate.
        Returns:
            y_int: interpolated value.
        """
        n = x.size
        x_int = symbols('x')
        y_int = 0

        for i in range(0, n):
            p = y[i]
            for j in range(0, n):
                if i != j:
                    p = p * (( x_int - x[j]) / (x[i] - x[j]))
            y_int = y_int + p
        
        return y_int

    def run(self):
        p = self.lagrange(self.x, self.y)
        p = simplify(p)
        return {
            'method_status': 'success',
            'result': {
                "pol": str(p)
            }
        }

'''
if __name__ == "__main__":
    x=[2,3,4,5,6]
    y=[2,6,5,5,6]
    print(Larange(x, y).run())

'''
