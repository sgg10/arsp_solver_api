class LinealSpline:
    def __init__(self, n, x, y):
        self.n = int(n)
        self.x = x
        self.y = y

    def run(self):
        respuesta = []
        for i in range(1, self.n):
            pendiente = (self.y[i] - self.y[i - 1]) / (self.x[i] - self.x[i - 1])
            resultado = (pendiente * -self.x[i]) + self.y[i]
            respuesta.append(f'P(X{i}) = {pendiente}X + {resultado}    {self.x[i - 1]} <= X <= {self.x[i]}')
        return {'result': respuesta}
