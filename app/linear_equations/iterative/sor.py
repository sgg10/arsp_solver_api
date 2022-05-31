#from app.utils.methods import BaseMethod
import numpy as np
from sympy import *

from app.utils.methods import BaseMethod


class SOR(BaseMethod):
    def __init__(self, A, b, omega, n, x0, tol, **kwargs):
        self.A = np.array(A)
        self.b = np.array(b)
        self.x0 = x0
        self.omega = float(omega)
        self.n = int(n)
        self.tol = float(tol)

    def sor_method(self, A, b, omega, n, x0, tol):
        x = np.zeros_like(b, dtype=np.double)

        iter1 = 0
        #Iterate
        for k in range(n):
            iter1 = iter1 + 1   
            x_old  = x.copy()
            
            #Loop over rows
            for i in range(A.shape[0]):
                x[i] = x[i]*(1-omega) + (omega/A[i,i])*(b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) 
                
            
            #Stop condition 
            #LnormInf corresponds to the absolute value of the greatest element of the vector.
            LnormInf = max(abs((x - x_old)))/max(abs(x_old)) 
            if  LnormInf < tol:
                break
         
        return x

    def run(self):
        x = self.sor_method(self.A, self.b, self.omega, self.n, self.x0, self.tol)
        return {'result': x}


'''

if __name__ == "__main__":
    A = [[4, 1, 1, 0, 1],[-1, -3, 1, 1, 0], [2, 1, 5, -1, -1], [-1, -2, -3, -4, 0], [0, 2, -1, 1, 4]]
    b = [6,6,6,6,6]
    x0 = [0,0,0,0,0]
    omega = 1.54
    N = 100
    tol = 0.0000007
    print(SOR( A, b, omega, N, x0, tol).run())
'''

    