from app.utils.methods import BaseMethod


class TotalPivot(BaseMethod):
    def __init__(self, n, A):
        self.n = int(n)
        self.A = A

    def swap_rows(self, A, higher_row, k):
        for i in range(len(A[0])):
            A[k][i], A[higher_row][i] = A[higher_row][i], A[k][i]
        return A

    def swap_columns(self, A, columnaMayor, k):
        for i in range(len(A[0])-1):
            A[i][k], A[i][columnaMayor] = A[i][columnaMayor], A[i][k]
        return A

    def backward_substitution(self, A, n):
        x = [0] * n
        for i in range(n-1, 0, -1):
            _sum = sum([A[i-1][p-1] * x[p-1] for p in range(i+1, n+1, 1)])
            x[i-1] = (A[i-1][n-1] - _sum) / A[i-1][i-1]
        return x

    def total_pivot(self, A, n, k):
        higher = 0
        higher_row = k
        higher_column = k
        for r in range(k,n):
            for s in range(k,n):
                if abs(A[r][s]) > higher:
                    higher = abs(A[r][s])
                    higher_row = r
                    higher_column = s
        if higher == 0:
            return ("El sistema no tiene solución única")
        else:
            if higher_row != k:
                A = self.swap_rows(A,higher_row,k)
            if higher_column != k:
                A = self.swap_columns(A,higher_column,k)
        return A

    def run(self):
        for k in range(1,self.n):
            self.A = self.total_pivot(self.A,self.n,k-1)
            for i in range(k, self.n):
                multiplier = float(self.A[i][k-1]/self.A[k-1][k-1])
                for j in range(k,self.n+2):
                    self.A[i][j-2] = self.A[i][j-2] - multiplier*self.A[k-1][j-2]
        return {
            "method_status": "success",
            'result': self.backward_substitution(self.A,self.n)
        }