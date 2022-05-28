from app.utils.methods import BaseMethod
import numpy as np
from numpy import size, eye, zeros


class PartialLU(BaseMethod):
    def __init__(self, A):
        self.A = np.array(A)

    def lu_factor(self, A):
        n = A.shape[0]
        piv = np.arange(0,n)
        for k in range(n-1):

            # piv
            max_row_index = np.argmax(abs(A[k:n,k])) + k
            piv[[k,max_row_index]] = piv[[max_row_index,k]]
            A[[k,max_row_index]] = A[[max_row_index,k]]

            # LU 
            for i in range(k+1,n):          
                A[i,k] = A[i,k]/A[k,k]      
                for j in range(k+1,n):      
                    A[i,j] -= A[i,k]*A[k,j] 

        return [A,piv]
        
    def ufsub(self,L,b):
        """ Unit row oriented forward substitution """
        for i in range(L.shape[0]): 
            for j in range(i):
                b[i] -= L[i,j]*b[j]
        return b

    def bsub(self,U,y):
        """ Row oriented backward substitution """
        for i in range(U.shape[0]-1,-1,-1): 
            for j in range(i+1, U.shape[1]):
                y[i] -= U[i,j]*y[j]
            y[i] = y[i]/U[i,i]
        return y

    def run(self):
        LU, piv = self.lu_factor(self.A)
        b = b[piv]
        proggresive_subst = self.ufsub(LU, b)
        back_subst = self.bsub( LU, proggresive_subst)
        return {"result": {"x": back_subst, "z": proggresive_subst, "LU": LU, "piv": piv}}
