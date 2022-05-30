from app.utils.methods import BaseMethod
import numpy as np
import math


class Cholesky(BaseMethod):
    def __init__(self, n, A, b, **kwargs):
        self.X = []
        self.U = []
        self.Z = []
        self.L = []

        self.n = int(n)
        self.A = A
        self.B = b

    def resolverMatriz(self, L, U, B, n):
        Y = [0] * n
        self.X = [0] * n
        for p in range(n):
            for k in range(n):
                if k == 0 and p == 0:
                    Ymn = B[k] / L[k][p]
                    Y[k] = Ymn
                elif k == p:
                    Ymn = B[k]
                    for t in range(k):
                        Ymn = Ymn - Y[t] * L[k][t]
                    Ymn = Ymn / L[k][p]
                    Y[k] = Ymn

        for p in range(n - 1, -1, -1):
            for k in range(n - 1, -1, -1):
                if k == 3 and p == 3:
                    Xmn = Y[k] / U[k][p]
                    self.X[k] = Xmn
                elif k == p:
                    Xmn = Y[k]
                    for t in range(1, 4):
                        Xmn = Xmn - self.X[t] * U[k][t]
                    Xmn = Xmn / U[k][p]
                    self.X[k] = Xmn
        return (self.X)

    def conversionL(self, A, L, U, B, n):
        for y in range(n):
            for x in range(n):
                if y == x:
                    if y == 0:
                        Lmn = float(math.sqrt(A[x][y]))
                        L[x][y] = Lmn
                        U[x][y] = Lmn
                    else:
                        Umn = A[x][y]
                        for t in range(y):
                            Umn = abs(Umn - L[x][t] * U[t][x])
                        Umn = float(math.sqrt(Umn))
                        L[x][y] = Umn
                        U[x][y] = Umn

                elif x > y:
                    if y == 0:
                        Lxy = A[x][y] / Lmn
                        L[x][y] = Lxy
                    else:
                        Lxy = A[x][y]
                        for t in range(y):
                            Lxy = Lxy - L[x][t] * U[t][y]
                        Lxy = Lxy / U[y][y]
                        L[x][y] = Lxy


                elif y > x:
                    if x == 0:
                        Uxy = A[x][y] / Lmn
                        U[x][y] = Uxy
                    else:
                        Uxy = A[x][y]
                        for t in range(y):
                            Uxy = Uxy - L[x][t] * U[t][y]
                        Uxy = Uxy / L[x][x]
                        U[x][y] = Uxy

        return self.resolverMatriz(L, U, B, n)

    def run(self):
        L = np.zeros([self.n, self.n])
        U = np.zeros([self.n, self.n])
        return {"x": [x[0] for x in self.conversionL(self.A, L, U, self.B, self.n)]}
