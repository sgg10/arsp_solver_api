from app.utils.methods import BaseMethod
import numpy as np


class SimpleLU(BaseMethod):
    def __init__(self, A, b, n, **kwargs):
        self.A = np.array(A).reshape(n, n)
        self.b = np.array(b).reshape(len(b), 1)
        self.n = n

    def proggresive_subst(self, M):
        n = len(M)
        x = np.zeros([n, 1])

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
        det = np.linalg.det(self.A)
        if det == 0:
            return {"Error": "Matrix must be nonsingular."}
        self.n = np.size(self.A, 1)
        L = np.eye(self.n)
        U = np.zeros((self.n, self.n))
        M = self.A
        result = {"iterations": [{"stage": 0, "M": list(map(lambda x: list(x), M))}]}
        for i in range(0, self.n - 1):
            for j in range(i + 1, self.n):
                if M[j, i] != 0:
                    L[j, i] = np.divide(M[j, i], M[i, i])
                    M[j, i:self.n] = np.subtract(M[j, i:self.n], (np.divide(M[j, i], M[i, i])) * M[i, i:self.n])
                U[i, i:self.n] = M[i, i:self.n]
                U[i + 1, i + 1:self.n] = M[i + 1, i + 1:self.n]
                result['iterations'].append({
                    "stage": i + 1,
                    "M": list(map(lambda x: list(x), M)),
                    "L": list(map(lambda x: list(x), L)),
                    "U": list(map(lambda x: list(x), U))
                })
        MLB = np.concatenate((L, self.b), axis=1)
        z = self.proggresive_subst(MLB)
        MUZ = np.concatenate((U, z), axis=1)
        result['result'] = list(map(lambda x: x[0], self.back_subst(MUZ)))
        return result
