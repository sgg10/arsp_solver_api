import numpy as np


class Doolittle:
    def __init__(self, n, A, B):
        self.X = []
        self.U = []
        self.Z = []
        self.L = []

        self.n = int(n)
        self.A = A
        self.B = B

    def run(self):
        self.L = np.zeros([self.n, self.n])
        self.U = np.zeros([self.n, self.n])
        for i in range(self.n):  # inicializa diagonal L con 1's
            self.L[i][i] = 1
        for k in range(self.n):  # Opera para encontrar la matriz L y U de A
            for j in range(k, self.n):
                sum = 0
                for p in range(k):
                    sum += self.L[k][p] * self.U[p][j]
                self.U[k][j] = (self.A[k][j] - sum) / self.L[k][k]
            for i in range(k, self.n):
                sum = 0
                for p in range(k):
                    sum += self.L[i][p] * self.U[p][k]
                self.L[i][k] = (self.A[i][k] - sum) / self.U[k][k]
        # ------Calcula Lz = B ----------#
        for i in range(self.n):
            sum = 0
            for j in range(i):
                sum += self.L[i][j] * self.Z[j]
            self.Z.append(self.B[i] - sum)

        # ------------Calcula Ux=Z----------------------#
        for i in range(self.n):
            self.X.append(0)
        for i in range(self.n - 1, 0 - 1, -1):
            sum = 0
            for j in range(i, self.n):
                sum += self.U[i][j] * self.X[j]
            self.X[i] = ((self.Z[i] - sum) / self.U[i][i])
        return (self.X)
