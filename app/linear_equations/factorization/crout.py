from app.utils.methods import BaseMethod
import numpy as np


class Croult(BaseMethod):
    def __init__(self, n, A, b, **kwargs):
        self.X = []
        self.U = []
        self.Z = []
        self.L = []

        self.n = n
        self.A = A
        self.B = b

    def run(self):
        stages = []
        self.n = int(self.n)
        self.L = np.zeros([int(self.n), int(self.n)])
        self.U = np.zeros([int(self.n), int(self.n)])
        for i in range(self.n):
            self.U[i][i] = 1
        for k in range(self.n):
            for i in range(k, self.n):
                sum = 0
                for p in range(k):
                    sum += self.L[i][p] * self.U[p][k]
                self.L[i][k] = (self.A[i][k] - sum) / self.U[k][k]
            for j in range(k, self.n):
                sum = 0
                for p in range(k):
                    sum += self.L[k][p] * self.U[p][j]
                self.U[k][j] = (self.A[k][j] - sum) / self.L[k][k]
            stages.append({
                "L": list(map(lambda x: list(x), self.L)),
                "U": list(map(lambda x: list(x), self.U)),
            })

        # ------------------Calcula Lz = B ----------#
        for i in range(self.n):
            sum = 0
            for j in range(i):
                sum += self.L[i][j] * self.Z[j]
            if i == 0:
                self.Z.append(self.B[i] / self.L[i][i])
            else:
                self.Z.append((self.B[i] - sum) /self. L[i][i])

        # ---------------Calcular Ux = B ---------#

        for i in range(self.n):
            self.X.append(0)
        for i in range(self.n - 1, 0 - 1, -1):
            sum = 0
            for j in range(i, self.n):
                sum += self.U[i][j] * self.X[j]
            self.X[i] = ((self.Z[i] - sum) / self.U[i][i])

        return {
            "method_status": "success",
            "result": {
                "stages": stages,
                "x": [x[0] for x in self.X],
                "z": [z[0] for z in self.Z]
            }
        }
