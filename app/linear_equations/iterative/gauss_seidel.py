from app.utils.methods import BaseMethod
import numpy as np

class GaussSeidel(BaseMethod):
    def __init__(self, A, b, x0, tolerance, iterations, **kwargs):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.x0 = np.array(x0, dtype=float)
        self.tol = tolerance
        self.iterations = iterations

    def diagnostics(self, a):
        diag = np.diag(np.abs(a)) 
        off_diag = np.sum(np.abs(a), axis=1) - diag 
        if np.all(diag > off_diag):
           return 1
        else:
            return 0

    def gauss_seidel(self,A,B,x,tol,iteramax):
        sz = np.shape(A)
        n = sz[0]
        m = sz[1]
        #  valores iniciales
        x = np.copy(x)
        difference = np.ones(n, dtype=float)
        bad = 2*tol

        itera = 0
        while not(bad<=tol or itera>iteramax):
            for i in range(0,n,1):
                add = 0
                for j in range(0,m,1):
                    if (i!=j):
                        add = add-A[i,j]*x[j]
                        
                nuevo = (B[i]+add)/A[i,i]
                difference[i] = np.abs(nuevo-x[i])
                x[i] = nuevo
            bad = np.max(difference)
            itera = itera + 1

        x = np.transpose([x])
        
        if (itera>iteramax):
                x=0
        return x

    def run(self):
        if self.diagnostics(self.A) == 0:
            return{"result":"Matrix is not diagonally dominant"}
        else:
            x = self.gauss_seidel(self.A, self.b, self.x0, self.tol, self.iterations)
            return {"result":{"x":x}}
        
'''
if __name__ == "__main__":
    A = [[-5, 2, 2],[2, 3, 0], [2, 0, 7]]
    b = [1,1,1]
    x = [0,0,0]
    N = 100
    tol = 10e-7
    print(GaussSeidel(A,b,x,tol,N).run())
''' 
