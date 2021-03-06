from app.utils.methods import BaseMethod
import numpy as np
import scipy
import scipy.linalg

class SimpleLU(BaseMethod):

    def __init__(self, A, b, **kwargs):
        self.b = np.array(b)
        self.P, self.L, self.U = scipy.linalg.lu(A)
        self.p = np.transpose(self.P)

    def back_substitution(self,U, y):
        
        n = U.shape[0]
        x = np.zeros_like(y, dtype=np.double);
        x[-1] = y[-1] / U[-1, -1]
        for i in range(n-2, -1, -1):
            x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
            
        return x
    
    def forward_substitution(self, L, b):

        n = L.shape[0]
        
        y = np.zeros_like(b, dtype=np.double);

        y[0] = b[0] / L[0, 0]
        
        for i in range(1, n):
            y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
            
        return y


    def run(self):
        y = self.forward_substitution(self.L, self.b)
        x = list(self.back_substitution(self.U, y))
        self.L = list(map(lambda _x: list(_x), self.L))
        self.U = list(map(lambda _x: list(_x), self.U))
        p = list(map(lambda _x: list(_x), np.transpose(self.P)))
        return {
            "method_status": "success",
            "result": {
                "L": self.L,
                "U": self.U,
                "P": p,
                "x": x
            }
        }



'''
if __name__ == "__main__":
    A =[
        [7, -2, -2, -1],
        [-2, 8, -2, -2],
        [-2, -2, 6, 2],
        [-1, -2, -2, 10]
        ]

    b = [1, 0, 4, 4]
    x = SimpleLU(A,b).run()

'''