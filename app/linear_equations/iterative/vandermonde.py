from app.utils.methods import BaseMethod 
from numpy import asarray, empty, promote_types, multiply
import numpy as np


class Vandermonde(BaseMethod):

    def __init__(self, x, y):
        self.x = asarray(x)
        self.y = asarray(y)

    def run(self):
        #Matrix of vandermonde 
        vandermonde = empty((len(self.x), len(self.x)), dtype=promote_types(self.x.dtype, self.y.dtype))
        for i in range(len(self.x)):
            vandermonde[i, :] = self.x ** i
        vandermonde = np.transpose(vandermonde[::-1])

        return {"result": {"vandermonde": vandermonde}}


    '''
    if __name__ == "__main__":
        x=[2,3,4,5,6]
        y=[2,6,5,5,6]
        print(Vandermonde(x, y).run())
    ''' 

