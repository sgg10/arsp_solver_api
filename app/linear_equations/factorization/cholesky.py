#from app.utils.methods import BaseMethod
import scipy
import scipy.linalg


class Cholesky():
    def __init__(self, A, **kwargs):
        self.A = A

    def run(self):
        L = scipy.linalg.cholesky(self.A, lower=True)
        U = scipy.linalg.cholesky(self.A, lower=False)
        print(L)
        print(U)
        return {'result': {"L: ":L,"U: ": U}}


if __name__ == "__main__":
    A =[
        [4, -1, 0, 3],
        [1, 15.5, 3, 8],
        [0, -1.3, -4, 1.1],
        [14, 5, -2, 30]
    ]
    print(Cholesky(A).run())