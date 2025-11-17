class Estrutura_um:

    def __init__(self, n, m):
        self.x_dim = n
        self.y_dim = m
        self.linha = dict()
        self.linha_t = dict()

    def checar_index(self, x, y):
        return x > self.x_dim or y > self.y_dim

    def acessar_elemento(self, i, j):
        if self.checar_index(i, j):
            return False
        
        if i in self.linha:
            coluna = self.linha[i]
            if j in coluna:
                return True
        
        return False

    def inserir_atualizar(self, i, j, valor):
        if self.checar_index(i, j):
            return False

        if i not in self.linha:
            self.linha[i] = dict()
        if j not in self.linha_t:
            self.linha_t[j] = dict()

        coluna = self.linha[i]
        coluna_t = self.linha_t[j]
        coluna[j] = valor
        coluna_t[i] = valor

        return True

    def retornar_transposta(self):
        return self.linha_t
    
    def soma_elemento(self, i, j, valor):
        self.linha[i][j] += valor
        self.linha_t[j][i] += valor

    def somar(self, matriz_b):
        if self.x_dim != matriz_b.x_dim or self.y_dim != matriz_b.y_dim:
            return False
        
        x = self.x_dim
        y = self.y_dim

        matriz_c = Estrutura_um(x, y)

        for r_index, coluna in self.linha.items():
            for c_index, valor in coluna.items():
                if not matriz_c.acessar_elemento(r_index, c_index):
                    matriz_c.inserir_atualizar(r_index, c_index, valor)
                else:
                    matriz_c.soma_elemento(r_index, c_index, valor)

        for r_index, coluna in matriz_b.linha.items():
            for c_index, valor in coluna.items():
                if not matriz_c.acessar_elemento(r_index, c_index):
                    matriz_c.inserir_atualizar(r_index, c_index, valor)
                else:
                    matriz_c.soma_elemento(r_index, c_index, valor)
        
        return matriz_c


    def multiplicar_escalar(self, escalar):
        for r_index, coluna in self.linha.items():
            for c_index, valor in coluna.items():
                self.linha[r_index][c_index] = valor * escalar

    def multiplicar_matriz(self, matriz_b):
        if self.y_dim != matriz_b.x_dim:
            return False
        
        matriz_c = Estrutura_um(self.x_dim, matriz_b.y_dim)

        for r_index_A, coluna_A in self.linha.items():
            for c_index_B, coluna_B in matriz_b.linha_t.items(): # pega colunas que tem valor usando a transposta de b
                counter = 0
                for c_index_A, valor_A in coluna_A.items():
                    if c_index_A in coluna_B:
                        a = valor_A
                        b = coluna_B[c_index_A]
                        counter += a*b
                matriz_c.inserir_atualizar(r_index_A, c_index_B, counter)

        return matriz_c


    def mostrar(self):
        for r, c in self.linha.items():
            print(f"linha {r}: {c}")
        print()

    def mostrar_t(self):
        for r, c in self.linha_t.items():
            print(f"linha {r}: {c}")
        print()



if __name__ == "__main__":
    matriz_a = Estrutura_um(5, 5)
    matriz_b = Estrutura_um(5, 5)

    matriz_a.inserir_atualizar(1, 1, 2)
    matriz_a.inserir_atualizar(2, 3, 5)
    matriz_b.inserir_atualizar(1, 1, 1)
    matriz_b.inserir_atualizar(4, 4, 5)
    matriz_b.inserir_atualizar(3, 1, 3)
    matriz_b.inserir_atualizar(3, 4, 4)

    matriz_c = matriz_a.multiplicar_matriz(matriz_b)
    matriz_c.mostrar()