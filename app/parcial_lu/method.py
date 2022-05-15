import numpy as np
from numpy import size, eye, zeros

class Parcial_LU:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        self.n = len(A)
        self.L = eye(self.n)
        self.U = zeros(self.n)
        self.P = eye(self.n)
        self.M = A

    def proggresive_subst(self, M):
        n = len(M)
        x = zeros([n, 1])

        x[0] = M[0, n] / M[0, 0]
        array = [[1]]
        for i in range(1, n):
            aux = np.concatenate((array, np.transpose(x[0:i])), axis=1)
            array_aux = [M[i - 1, n]]
            aux_ = np.concatenate((array_aux, -M[i, 0:i]), axis=0)
            x[i] = np.dot(aux, aux_) / M[i, i]
        return x

    def back_subst(self, M):
        n = len(M)
        x = np.ones([n, 1])
        for i in range(n - 1, -1, -1):
            value = 0
            for j in range(i + 1, n):
                value += M[i, j] * x[j]
            x[i] = (M[i, n] - value) / M[i, i]
        return x

    def run(self):
        for i in range(1, self.n - 1):
            aux0, aux = max(abs(self.M[i + 1:self.n, i]))
            if aux0 > abs(self.M(i, i)):
                aux2 = self.M[i + aux, i:self.n]
                aux3 = self.P[i + aux, i:self.n]
                self.M[aux + i, i:self.n] = self.M[i, i:self.n]
                self.P[aux + i, :] = self.P[i, :]
                self.M[i, i:self.n] = self.P[i, :]
                self.P[i, :] = aux3
                if i > 1:
                    aux4 = self.L[i + aux, 1:i - 1]
                    self.L[i + aux, 1:i - 1] = self.L[i, 1:i - 1]
                    self.L[i, 1:i - 1] = aux4
            for j in range(i + 1, self.n):
                if self.M[j, i] != 0:
                    self.L[j, i] = self.M[j, i] / self.M[i, i]
                    self.M[j, i:self.n] = self.M[j, i:self.n] - self.M[j, i] / self.M[i, i] * self.M[i, i:self.n]
            self.U[i, i:self.n] = self.M[i, i:self.n]
            self.U[i + 1, i + 1:self.n] = self.M[i + 1, i + 1:self.n]

        return {"result": {"x": self.back_subst(self.U), "z": self.proggresive_subst(self.L)}}
