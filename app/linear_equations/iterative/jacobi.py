from app.utils.methods import BaseMethod


class Jacobi(BaseMethod):
    def __init__(self, n, A, b, x0, iterations, tolerance, **kwargs):
        self.n = int(n)
        self.A = A
        self.b = b
        self.x0 = x0
        self.niter = float(iterations)
        self.tolerancia = float(tolerance)
        self.vector = []

    def run(self):
        contador = 0
        dispersion = self.tolerancia + 1
        x1 = []
        self.vector.append([str(contador), str(self.x0), str(dispersion)])
        while dispersion > self.tolerancia and contador < self.niter:
            x1 = self.calcularNuevoJacobi(self.x0, self.n, self.b, self.A)
            dispersion = self.norma(x1, self.x0, self.n)
            self.x0 = x1
            contador += 1
            self.vector.append([str(contador), str(self.x0), str(dispersion)])

        if dispersion < self.tolerancia:
            return (f'{x1} es una aproximación con una tolerancia: {self.tolerancia}')
        else:
            return {"result": x1}

    def calcularNuevoJacobi(self, x0, n, b, A):
        x1 = []
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    valor = x0.pop(j)
                    x0.insert(j, valor)
                    suma += A[i][j] * valor[0] if type(valor) == list else valor

            valor = b[i][0]
            elemento = (valor - suma) / A[i][i]
            x1.append(elemento)
        return x1

    def norma(self, x1, x0, n):
        mayor = -1
        for i in range(n):
            valor0 = x0[i]
            valor0 = valor0[0] if type(valor0) == list else valor0
            valor1 = x1[i]
            if abs(valor1 - valor0) > mayor:
                mayor = abs(valor1 - valor0) / abs(valor1)
        return mayor
