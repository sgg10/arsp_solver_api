#from app.utils.methods import BaseMethod
import numpy as np
from sympy import Q, symbols, Function, Symbol, diff, solve
import math
from scipy.interpolate import interp1d 

class QuadraticSpline():

    def __init__(self, x, y, **keywords):
        self.x = x
        self.y = y

    def run(self):
        f= interp1d(self.x, self.y, kind='quadratic')
        
        return {'result': f}


if __name__ == "__main__":
    x=[2,3,4,5,6]
    y=[2,6,5,5,6]
    print(QuadraticSpline(x, y).run())
