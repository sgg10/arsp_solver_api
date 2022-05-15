from app.utils.methods import BaseMethod


class GaussianElimination(BaseMethod):

    def __init__(self, n, A):
        self.n = int(n)
        self.A = A
        self.array = []
        self.matrixs = []
        self.targets = []
        self.multipliers = []
        # self.convert_to_array = lambda matrix: [matrix[row] for row in sorted(list(matrix))]

    def backward_substitution(self, A, n):
        x = [0] * n
        for i in range(n - 1, 0, -1):
            _sum = sum([A[i - 1][p - 1] * x[p - 1] for p in range(i + 1, n + 1, 1)])
            x[i - 1] = (A[i - 1][n - 1] - _sum) / A[i - 1][i - 1]
        return x

    def run(self):
        A = self.A
        for k in range(1, self.n):
            self.targets.append(f'Stage {k}. Target: put zeros under element A {k}{k} = {A[k - 1][k - 1]}')
            for i in range(k, self.n):
                multiplier = float(A[i][k - 1] / A[k - 1][k - 1])
                self.multipliers.append(f'M{i}{k} = {multiplier}')
                for j in range(k, self.n + 1):
                    A[i][j - 1] = A[i][j - 1] - multiplier * A[k - 1][j - 1]
                self.matrixs.append(str(A))
        return {
            "method_status": "success",
            "result": self.backward_substitution(A, self.n),
            "matrixs_iterations": self.matrixs
        }
