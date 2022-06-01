#from app.utils.methods import BaseMethod
from numpy import array, zeros, diag, diagflat, dot
from sympy import jacobi

from app.utils.methods import BaseMethod

class Jacobi(BaseMethod):
    def __init__(self, A, b, n, x0=None, tol=1e-7, **kwargs):
        self.A = A
        self.b = b
        self.n = int(n)
        self.x0 = x0
        self.tol = float(tol)

    def jacobi(self, A, b, x0, n, tol):
        iters = []
        x = x0
        if x0 is None:
            x0 = zeros(len(A[0]))
        D = diag(A)
        R = A - diagflat(D)

        for i in range(n):
            x0 = (b - dot(R, x)) / D
            if abs(x0 - x).max() < tol:
                break
            x = x0
            iters.append(list(x0))
        return {
            "x": list(x0),
            "iterations": iters
        }

    def run(self):
        x = self.jacobi(self.A, self.b, self.x0, self.n, self.tol)
        return {
            'method_status': 'success',
            'result': x
        }


'''
if __name__ == "__main__":
    A = [[4, 1, 1, 0, 1],[-1, -3, 1, 1, 0], [2, 1, 5, -1, -1], [-1, -2, -3, -4, 0], [0, 2, -1, 1, 4]]
    b = [6,6,6,6,6]
    x = [0,0,0,0,0]
    N = 100
    tol = 0.0000007
    print(Jacobi( A, b, N, x, tol).run())
'''
