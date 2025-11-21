import time
import random
import csv
import tracemalloc
from estrutura_dois import EstruturaDois
from estrutura_um import Estrutura_um
from matriz_tradicional import MatrizTradicional

class ComparadorEstruturas:

    @staticmethod
    def medir_tempo_memoria(funcao, *args):
        tracemalloc.start()
        inicio = time.time()
        resultado = funcao(*args)
        fim = time.time()
        _, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return fim - inicio, memoria_pico, resultado

    @staticmethod
    def salva_csv(nome_arquivo, resultados, dimensao, esparsidade):
        estruturas = ["EstruturaUm", "EstruturaDois", "MatrizTradicional"]
        operacoes = list(resultados.keys())

        with open(nome_arquivo, mode='a', newline='') as arquivo:
            writer = csv.writer(arquivo)

            if arquivo.tell() == 0:
                writer.writerow(["Dimensão", "Esparsidade", "Operação"] + [f"{estrutura} Tempo (s)" for estrutura in estruturas] + [f"{estrutura} Memória (bytes)" for estrutura in estruturas])

            for operacao in operacoes:
                linha = [dimensao, esparsidade, operacao]
                for estrutura in estruturas:
                    tempo, memoria = resultados[operacao][estrutura]
                    linha.append(f"{tempo:.6f}")
                    linha.append(memoria)
                writer.writerow(linha)

    @staticmethod
    def gera_matrizes(dimensao, esparsidade):
        matriz_um = Estrutura_um(dimensao, dimensao)
        matriz_dois = EstruturaDois(dimensao, dimensao)
        matriz_tradicional = MatrizTradicional(dimensao, dimensao)

        elementos_nao_nulos = int(dimensao * dimensao * esparsidade)
        for _ in range(elementos_nao_nulos):
            i, j = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
            valor = random.randint(1, 100)
            matriz_um.inserir_atualizar(i, j, valor)
            matriz_dois.inserir_atualizar(i, j, valor)
            matriz_tradicional.inserir_atualizar(i, j, valor)

        return matriz_um, matriz_dois, matriz_tradicional

    @staticmethod
    def comparar_operacoes(dimensao: int, esparsidade: float):
        print(f"\nComparando estruturas para dimensão {dimensao}x{dimensao} e esparsidade {esparsidade * 100}%")

        matriz_um, matriz_dois, matriz_tradicional = ComparadorEstruturas.gera_matrizes(dimensao, esparsidade)

        operacoes = [
                ("Acessar elemento", 1, lambda m: m.acessar_elemento(0, 0)),
                ("Inserir/atualizar elemento", 1, lambda m: m.inserir_atualizar(0, 0, 42)),
                ("Mostrar transposta", 1, lambda m: m.mostrar_t()),
                ("Multiplicação por escalar", 1, lambda m: m.multiplicar_escalar(2)),
                ("Soma de matrizes", 2, lambda m1, m2: m1.somar(m2)),
                ("Multiplicação de matrizes", 2, lambda m1, m2: m1.multiplicar_matriz(m2)),
            ]


        resultados = {}

        for nome, num_argumentos, operacao in operacoes:
            resultados[nome] = {}
            print(f"\nOperação: {nome}")

            for estrutura, nome_estrutura in zip(
                [matriz_um, matriz_dois, matriz_tradicional],
                ["EstruturaUm", "EstruturaDois", "MatrizTradicional"]
            ):
                if (num_argumentos == 1):
                    tempo, memoria, _ = ComparadorEstruturas.medir_tempo_memoria(
                        operacao, estrutura
                    )
                else:
                    tempo, memoria, _ = ComparadorEstruturas.medir_tempo_memoria(
                        operacao, estrutura, estrutura
                    )

                print(f"{nome_estrutura}: {tempo:.6f}s, {memoria} bytes")
                resultados[nome][nome_estrutura] = (tempo, memoria)

        ComparadorEstruturas.salva_csv("resultados_completos.csv", resultados, dimensao, esparsidade)

def main():
    dimensoes = [10**i for i in range(2, 7)]

    for i, dimensao in enumerate(dimensoes, start=2):
        if (i >= 4):
            esparsidades = [
                1 / 10**(i + 4),
                1 / 10**(i + 3),
                1 / 10**(i + 2),
            ]
        else:
            esparsidades = [0.01, 0.05, 0.1, 0.2]

        for esparsidade in esparsidades:
            ComparadorEstruturas.comparar_operacoes(dimensao, esparsidade)

if __name__ == "__main__":
    main()