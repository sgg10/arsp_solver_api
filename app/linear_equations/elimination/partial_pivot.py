from app.utils.methods import BaseMethod
import numpy as np

class PartialPivot(BaseMethod):

    def __init__(self, A, b, **kwargs):
        self.a = A
        self.b = b

    def linearsolver(self,A,b):
        n = len(A)
        M = A

        i = 0
        for x in M:
            x.append(b[i])
            i += 1

        iterations = []
        for k in range(n):
            for i in range(k,n):
                if abs(M[i][k]) > abs(M[k][k]):
                    M[k], M[i] = M[i],M[k]
                else:
                    pass

            for j in range(k+1,n):
                q = float(M[j][k]) / M[k][k]
                for m in range(k, n+1):
                    M[j][m] -=  q * M[k][m]

            iterations.append([row for row in M])

        x = [0 for i in range(n)]

        x[n-1] =float(M[n-1][n])/M[n-1][n-1]
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z = z  + float(M[i][j])*x[j]
            x[i] = float(M[i][n] - z)/M[i][i]

        return {
            'x': x,
            'stages': iterations
        }

    def run(self):
        result = self.linearsolver(self.a, self.b)
        return {
            "method_status": 'success',
            "result": result
        }

'''
if __name__ == "__main__":
    A =[
        [4, -1, 0, 3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]
        ]

    b = [1, 2, 3, 4]
    PartialPivot(A, b).run()

'''


