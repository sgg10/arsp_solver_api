from app.utils.methods import BaseMethod


class GaussSeidel(BaseMethod):
    def __init__(self, n, A, b, x0, niter, tol):
        self.n = int(n)
        self.A = A
        self.b = b
        self.x0 = x0
        self.tol = float(tol)
        self.niter = float(niter)
        self.vector = []

    def calcularNuevoGaussSeidel(self, x0, n, b, A):
        x1 = []
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    valor = x0
                    x0.insert(j, valor)
                    suma += A[i][j] * valor
            valor = b.pop(i)
            b.insert(i, valor)
            elemento = (valor - suma) / A[i][i]
            x1.append(elemento)
            x0.pop(i)
            x0.insert(i, elemento)
        return x1

    def norma(self, x1, x0, n):
        mayor = -1
        for i in range(n):
            valor0 = x0[i]
            valor1 = x1[i]
            if abs(valor1 - valor0) > mayor:
                mayor = abs(valor1 - valor0) / abs(valor1)
        return mayor

    def run(self):
        contador = 0
        dispersion = self.tol + 1
        x1 = []
        self.vector.append([str(contador), str(self.x0), str(dispersion)])
        while contador < self.niter:
            x1 = self.calcularNuevoGaussSeidel(self.x0, self.n, self.b, self.A)
            dispersion = self.norma(x1, self.x0, self.n)
            self.x0 = x1
            contador += 1
            self.vector.append([str(contador), str(self.x0), str(dispersion)])
        return (x1)
