from app.utils.methods import BaseMethod
import scipy
import scipy.linalg


class Cholesky(BaseMethod):
    def __init__(self, A, **kwargs):
        self.A = A

    def run(self):
        L = scipy.linalg.cholesky(self.A, lower=True)
        U = scipy.linalg.cholesky(self.A, lower=False)
        print(L)
        print(U)
        return {'result': {"L: ":L,"U: ": U}}
