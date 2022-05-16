import numpy as np
from app.utils.methods import BaseMethod


class GaussianElimination(BaseMethod):
    def __init__(self, A, b):
        self.A = np.array(A)
        self.A = np.array(A, dtype=float)
        self.b = np.array(b)
        self.AB = np.concatenate((self.A, self.b), axis=1)
        self.n, self.m = np.shape(self.AB)

    def swap_rows(self, AB):
        for i in range(0, self.n-1, 1):
            col = abs(AB[i:, i])
            _max = np.argmax(col)

            if _max != 0:
                tmp = np.copy(AB[i, :])
                AB[i, :] = AB[_max + i, :]
                AB[_max + i, :] = tmp
            print(AB)
        return AB

    def forward_elimination(self, AB):
        stages = []
        for i in range(0, self.n - 1, 1):
            pivot = AB[i, i]
            forward = i + 1
            for k in range(forward, self.n, 1):
                factor = AB[k, i]/pivot
                AB[k, :] = AB[k, :] - AB[i, :]*factor
            stages.append(list(map(lambda x: list(x), AB)))
        return AB, stages

    def backward_elimination(self, AB):
        last_row = self.n - 1
        last_col = self.m - 1
        for i in range(last_row, -1, -1):
            pivot = AB[i, i]
            back = i - 1
            for k in range(back, -1, -1):
                factor = AB[k, i] / pivot
                AB[k, :] = AB[k, :] - AB[i, :]*factor
            AB[i, :] = AB[i, :] / AB[i, i]
        x = np.copy(AB[:, last_col])
        x = np.transpose([x])
        return AB, x

    def run(self):
        AB0 = self.swap_rows(self.AB)
        AB1, stages = self.forward_elimination(AB0)
        AB2, X = self.backward_elimination(AB1)
        AB2 = list(map(lambda x: list(x), AB2))
        X = list(map(lambda x: x[0], X))
        return self.success_response({"x": X, "stages": stages})
