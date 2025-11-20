class MatrizTradicional:
    def __init__(self, n: int, m: int):
        self.x_dim = n
        self.y_dim = m
        self.matriz = [[0 for _ in range(m)] for _ in range(n)]

    def acessar_elemento(self, i: int, j: int) -> int:
        return self.matriz[i][j]

    def inserir_atualizar(self, i: int, j: int, valor: int):
        self.matriz[i][j] = valor

    def somar(self, matriz_b):
        if ((self.x_dim != matriz_b.x_dim) or (self.y_dim != matriz_b.y_dim)):
            return False

        resultado = MatrizTradicional(self.x_dim, self.y_dim)
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                resultado.inserir_atualizar(i, j, self.matriz[i][j] + matriz_b.acessar_elemento(i, j))
        return resultado

    def multiplicar_escalar(self, escalar: int):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                self.matriz[i][j] *= escalar

    def multiplicar_matriz(self, segunda_matriz):

        if (self.y_dim != segunda_matriz.x_dim):
            return False

        resultado = MatrizTradicional(self.x_dim, segunda_matriz.y_dim)
        for i in range(self.x_dim):
            for j in range(segunda_matriz.y_dim):
                soma = 0
                for k in range(self.y_dim):
                    soma += self.matriz[i][k] * segunda_matriz.acessar_elemento(k, j)
                resultado.inserir_atualizar(i, j, soma)
                
        return resultado

    def mostrar_t(self):

        transposta = MatrizTradicional(self.y_dim, self.x_dim)
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                transposta.inserir_atualizar(j, i, self.matriz[i][j])

        return transposta
    
    def mostrar(self):
        for linha in self.matriz:
            print(linha)