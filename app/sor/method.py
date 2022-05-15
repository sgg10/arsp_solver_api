from numpy import *
from sympy import *


class SOR:
    def __init__(self, n, A, b, x0, omega, nIter, tol):
        self.n = int(n)
        self.A = A
        self.b = b
        self.x0 = x0
        self.omega = float(omega)
        self.nIter = int(nIter)
        self.tol = float(tol)

    def calcularNuevoJacobi(self, x0, n, b, A, omega):
        x1 = []
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    valor = x0.pop(j)
                    x0.insert(j, valor)
                    suma += A[i][j] * valor

                valor = b[i]
                original = x0[i]
                elemento = (valor - suma) / A[i][i]
                r = omega * elemento + (1 - omega) * original
                x1.append(r)
        return x1

    def normaEuclidiana(self, x1, x0, n):
        sumaCuadrados = 0
        for i in range(n):
            valor0 = x0[i]
            valor1 = x1[i]
            sumaCuadrados += (valor1 - valor0) ** 2

        return sqrt(sumaCuadrados)

    def run(self):
        contador = 0
        dispersion = self.tol + 1
        x1 = []
        print('Orden de los datos: n, x1, x2, x3, ... xn, dispersion')
        iters = [{'contador': contador, 'x0': self.x0}]
        while dispersion > self.tol and contador < self.nIter:
            x1 = self.calcularNuevoJacobi(self.x0, self.n, self.b, self.A, self.omega)
            dispersion = self.normaEuclidiana(x1, self.x0, self.n)
            self.x0 = x1
            contador += 1
            iters.append({'contador': contador, 'x0': self.x0, 'dispersion': dispersion})
        if dispersion < self.tol:
            return {'result': f'{x1} es una aproximacion con una toleracia de: {self.tol}', 'iters': iters}
        else:
            return {'result': f'Fracaso en {self.nIter} iteraciones', 'iters': iters}
