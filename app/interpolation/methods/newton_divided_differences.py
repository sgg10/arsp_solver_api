from app.utils.methods import BaseMethod
from audioop import reverse
from typing import List
from sympy import Function, expand
from sympy.parsing.sympy_parser import parse_expr
import numpy as np



class NewtonDifDiv(BaseMethod):

    def __init__(self, x, y ):
        self.x = np.array(x)
        self.y = np.array(y)
        

    def divided_diff(self, x, y):
        '''
        function to calculate the divided
        differences table
        '''
        n = x.size
        q = np.zeros((n, n - 1))

        # Insert 'y' in the first column of the matrix 'q'
        q = np.concatenate((y[:, None], q), axis=1)

        for i in range(1, n):
            for j in range(1, i + 1):
                q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

        # Copy the diagonal values of the matrix q to the vector f
        f = np.zeros(n)
        for i in range(0, n):
            f[i] = q[i, i]

        # Prints the polynomial
        pol = '{}'.format("p(x)={:+.4f}".format(f[0]), end="")
        for i in range(1, n):
            pol += '{}'.format("{:+.4f}".format(f[i]), end="")
            for j in range(1, i + 1):
                pol += '{}'.format("(x{:+.4f})".format(x[j] * -1), end="")

        
        return q,[f],pol

    def run(self):
        m,coef, pol = self.divided_diff(self.x, self.y)
        return {"result": {"Matrix":m, "Coef": coef, "Pol": pol}}

"""
if __name__ == "__main__":
    x=[2,3,4,5,6]
    y=[2,6,5,5,6]
    print(NewtonDifDiv(x, y).run())
"""
