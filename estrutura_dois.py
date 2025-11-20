from arvore_avl import ArvoreAVL

class EstruturaDois:
    def __init__(self, n, m):
        self.x_dim = n
        self.y_dim = m
        self.linhas = ArvoreAVL()
        self.colunas = ArvoreAVL()

    def indice_invalido(self, x, y):
        return (x >= self.x_dim) or (y >= self.y_dim)

    def acessar_elemento(self, i, j):

        if self.indice_invalido(i, j):
            return 0

        linha = self.linhas.busca_no(self.linhas.raiz, i)
        if linha:
            coluna = linha.valor.busca_no(linha.valor.raiz, j)
            if coluna:
                return coluna.valor
        return 0

    def inserir_atualizar(self, i, j, valor):
        if (self.indice_invalido(i, j)):
            return False

        linha = self.linhas.busca_no(self.linhas.raiz, i)
        if (not linha):
            nova_linha = ArvoreAVL()
            nova_linha.raiz = nova_linha.insere_no(nova_linha.raiz, j, valor)
            self.linhas.raiz = self.linhas.insere_no(self.linhas.raiz, i, nova_linha)
        else:
            linha.valor.raiz = linha.valor.insere_no(linha.valor.raiz, j, valor)

        coluna_node = self.colunas.busca_no(self.colunas.raiz, j)
        if (not coluna_node):
            nova_coluna = ArvoreAVL()
            nova_coluna.raiz = nova_coluna.insere_no(nova_coluna.raiz, i, valor)
            self.colunas.raiz = self.colunas.insere_no(self.colunas.raiz, j, nova_coluna)
        else:
            coluna_node.valor.raiz = coluna_node.valor.insere_no(coluna_node.valor.raiz, i, valor)

        return True

    def somar(self, segunda_matriz: 'EstruturaDois'):
        if ((self.x_dim != segunda_matriz.x_dim) or (self.y_dim != segunda_matriz.y_dim)):
            return False

        matriz_resultante = EstruturaDois(self.x_dim, self.y_dim)

        for i, linha in self.linhas.imprime_ordenado(self.linhas.raiz):
            for j, valor in linha.imprime_ordenado(linha.raiz):
                matriz_resultante.inserir_atualizar(i, j, valor)

        for i, linha in segunda_matriz.linhas.imprime_ordenado(segunda_matriz.linhas.raiz):
            for j, valor in linha.imprime_ordenado(linha.raiz):
                soma = matriz_resultante.acessar_elemento(i, j) + valor
                matriz_resultante.inserir_atualizar(i, j, soma)

        return matriz_resultante

    def multiplicar_escalar(self, escalar):
        raizes = [self.linhas.raiz, self.colunas.raiz]

        for raiz_atual in raizes:
            if (not raiz_atual):
                continue
            
            pilha_externa = [raiz_atual]
            
            while (pilha_externa):
                no_externo = pilha_externa.pop()
                
                if(no_externo):
                    pilha_externa.append(no_externo.esquerda)
                    pilha_externa.append(no_externo.direita)

                    pilha_interna = [no_externo.valor.raiz]
                    
                    while (pilha_interna):
                        no_interno = pilha_interna.pop()
                        
                        if no_interno:
                            pilha_interna.append(no_interno.esquerda)
                            pilha_interna.append(no_interno.direita)

                            no_interno.valor *= escalar

    def multiplicar_matriz(self, segunda_matriz):
        if (self.y_dim != segunda_matriz.x_dim):
            return False

        matriz_resultante = EstruturaDois(self.x_dim, segunda_matriz.y_dim)

        for indice_linha_primeira, linha_primeira in self.linhas.imprime_ordenado(self.linhas.raiz):
            for indice_coluna_primeira, valor_primeira in linha_primeira.imprime_ordenado(linha_primeira.raiz):

                no_linha_segunda = segunda_matriz.linhas.busca_no(
                    segunda_matriz.linhas.raiz,
                    indice_coluna_primeira
                )
                if (not no_linha_segunda):
                    continue

                for indice_coluna_segunda, valor_segunda in no_linha_segunda.valor.imprime_ordenado(no_linha_segunda.valor.raiz):
                    novo_valor = (
                        matriz_resultante.acessar_elemento(indice_linha_primeira, indice_coluna_segunda)
                        + valor_primeira * valor_segunda
                    )
                    matriz_resultante.inserir_atualizar(
                        indice_linha_primeira,
                        indice_coluna_segunda,
                        novo_valor
                    )

        return matriz_resultante


    def mostrar_t(self):
        t = EstruturaDois(self.y_dim, self.x_dim)
        t.linhas = self.colunas
        t.colunas = self.linhas
        return t

    def mostrar(self):
        for i, arvore in self.linhas.imprime_ordenado(self.linhas.raiz):
            print(f"Linha {i}: ", end="")
            for j, valor in arvore.imprime_ordenado(arvore.raiz):
                print(f"({j}: {valor}) ", end="")
            print()
        print()
