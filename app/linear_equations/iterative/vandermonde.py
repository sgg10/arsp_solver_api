from app.utils.methods import BaseMethod
from numpy import asarray, empty, promote_types, multiply


class Vandermonde(BaseMethod):

    def __init__(self, x):
        self.x = asarray(x)

    def run(self):
        if self.x.ndim != 1:
            raise ValueError('x must be a one-dimensional array or sequence.')
        N = len(self.x)
        v = empty((N, N), dtype=promote_types(self.x.dtype, int))
        temp = v[:, ::-1]

        if N > 0:
            temp[:, 0] = 1
        if N > 1:
            temp[:, 1:] = self.x[:, None]
            multiply.accumulate(temp[:, 1:], out=temp[:, 1:], axis=1)
        result = str(v).replace('\n ', ',')
        return {'result': result}
