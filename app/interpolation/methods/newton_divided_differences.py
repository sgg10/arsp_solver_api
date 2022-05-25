from app.utils.methods import BaseMethod
from sympy import Function, expand
from sympy.parsing.sympy_parser import parse_expr


class NewtonDifDiv(BaseMethod):
    def __init__(self, n, table):
        self.n = int(n)
        self.tabla = table

    def run(self):
        polinimio = f'P(X) = {self.tabla[0][1]}'
        F = Function('F')
        for j in range(2, self.n + 1):
            for i in range(j - 1, self.n):
                self.tabla[i][j] = (self.tabla[i][j - 1] - self.tabla[i - 1][j - 1]) / (
                            self.tabla[i][0] - self.tabla[i - j + 1][0])
                if i == j - 1:
                    polinimio += f' + {self.tabla[i][j]}'
                    for k in range(0, i):
                        print(f'i={i} j={j} k={k}')
                        polinimio += f'(x - {self.tabla[k][0]})'
        F = parse_expr(polinimio.replace('P(X) = ', '').replace('(', '*('))
        self.printTabla(self.tabla, self.n)
        return {
            'result': f'P(x) = {expand(F)}',
            'schematic_form': polinimio
        }

    def printTabla(self, tabla, n):
        print(
            "n |   xi   |      f[xi]     |         primera         |          Segunda          |          Tercera     "
            "     |         Cuarta         |         Quinta        |Nesima|")
        for i in range(n):
            print(str(i) + "     " + str(tabla[i]).replace("'", " ").replace(",", "       ").replace("[", " ").replace(
                "]", " ").replace(" 0 ", " "))
            print("\n")
