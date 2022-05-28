from app.utils.methods import BaseMethod
import scipy
import scipy.linalg
import numpy as np

class PartialLU(BaseMethod):
    def __init__(self, A):
        self.P, self.L, self.U = scipy.linalg.lu(A)
    def run(self):
        
        return {"result": {"L": self.L, "U": self.U, "P": np.transpose(self.P)}}

if __name__ == "__main__":
    A = [[2,4,3,-2],[4,9,7,-3],[-2,-3,2,7]]
    print(PartialLU(A).run())