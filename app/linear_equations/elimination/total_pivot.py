#from app.utils.methods import BaseMethod
from utils import regresiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import swapCols
from utils import isSquared
from numpy import array, zeros, fabs, linalg
import numpy as np
import ast, json
class TotalPivot():

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

        for k in range(n):
            print("iteration: ", k)
            for i in range(k,n):
                if abs(M[i][k]) > abs(M[k][k]):
                    M[k], M[i] = M[i],M[k]
                else:
                    pass

            for j in range(k+1,n):
                q = float(M[j][k]) / M[k][k]
                for m in range(k, n+1):
                    M[j][m] -=  q * M[k][m]
            
            for row in M:
                print(row)

        x = [0 for i in range(n)]

        x[n-1] =float(M[n-1][n])/M[n-1][n-1]
        for i in range (n-1,-1,-1):
            z = 0
            for j in range(i+1,n):
                z = z  + float(M[i][j])*x[j]
            x[i] = float(M[i][n] - z)/M[i][i]
            
        print('Coefficients: ')
        print(x)

    def run(self):
        self.linearsolver(self.a, self.b)

        #return {'result': {"coef: ": x}}


if __name__ == "__main__":
    A =[
        [4, -1, 0, 3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]
        ]

    b = [1, 2, 3, 4]
    TotalPivot(A, b).run()