import time
import random
import csv
import tracemalloc
from estrutura_dois import EstruturaDois
from estrutura_um import Estrutura_um
from matriz_tradicional import MatrizTradicional
import gc

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
                writer.writerow([
                    "Dimensão", "Esparsidade", "Operação",
                    "EstruturaUm Tempo (s)", "EstruturaUm Memória (bytes)",
                    "EstruturaDois Tempo (s)", "EstruturaDois Memória (bytes)",
                    "MatrizTradicional Tempo (s)", "MatrizTradicional Memória (bytes)"
                ])

            for operacao in operacoes:
                linha = [dimensao, esparsidade, operacao]
                for estrutura in estruturas:
                    tempo, memoria = resultados[operacao][estrutura]
                    linha.append(f"{tempo:.6f}")
                    linha.append(memoria)
                writer.writerow(linha)

    @staticmethod
    def gera_matrizes(dimensao, esparsidade):
        gerar_tradicional = dimensao <= 10**3

        matriz_um = Estrutura_um(dimensao, dimensao)
        matriz_dois = EstruturaDois(dimensao, dimensao)
        matriz_tradicional = MatrizTradicional(dimensao, dimensao) if gerar_tradicional else None

        elementos_nao_nulos = int(dimensao * dimensao * esparsidade)
        for _ in range(elementos_nao_nulos):
            i, j = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
            valor = random.randint(1, 100)
            matriz_um.inserir_atualizar(i, j, valor)
            matriz_dois.inserir_atualizar(i, j, valor)
            if gerar_tradicional:
                matriz_tradicional.inserir_atualizar(i, j, valor)

        return matriz_um, matriz_dois, matriz_tradicional

    @staticmethod
    def comparar_operacoes(dimensao: int, esparsidade: float):
        print(f"\nComparando estruturas para dimensão {dimensao}x{dimensao} e esparsidade {esparsidade * 100}%")

        operacoes = [
            ("Acessar elemento", lambda m: m.acessar_elemento(0, 0)),
            ("Inserir/atualizar elemento", lambda m: m.inserir_atualizar(0, 0, 42)),
            ("Retornar transposta", lambda m: m.retornar_transposta()),
            ("Multiplicação por escalar", lambda m: m.multiplicar_escalar(2)),
            ("Soma de matrizes", lambda m: m.somar_matrizes(m)),
            ("Multiplicação de matrizes", lambda m: m.multiplicar_matriz(m)),
        ]

        resultados = {}

        for nome, operacao in operacoes:
            resultados[nome] = {}
            print(f"\nOperação: {nome}")

            # Estrutura 1
            matriz_um = Estrutura_um(dimensao, dimensao)
            elementos_nao_nulos = int(dimensao * dimensao * esparsidade)
            for _ in range(elementos_nao_nulos):
                i, j = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
                valor = random.randint(1, 100)
                matriz_um.inserir_atualizar(i, j, valor)

            tempo, memoria, _ = ComparadorEstruturas.medir_tempo_memoria(operacao, matriz_um)
            print(f"EstruturaUm: {tempo:.6f}s, {memoria} bytes")
            resultados[nome]["EstruturaUm"] = (tempo, memoria)
            del matriz_um
            gc.collect()

            # Estrutura 2
            matriz_dois = EstruturaDois(dimensao, dimensao)
            for _ in range(elementos_nao_nulos):
                i, j = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
                valor = random.randint(1, 100)
                matriz_dois.inserir_atualizar(i, j, valor)

            tempo, memoria, _ = ComparadorEstruturas.medir_tempo_memoria(operacao, matriz_dois)
            print(f"EstruturaDois: {tempo:.6f}s, {memoria} bytes")
            resultados[nome]["EstruturaDois"] = (tempo, memoria)
            del matriz_dois
            gc.collect()

            # Matriz Tradicional (até 10**3 para evitar matrizes densas de dimensão alta)
            if (dimensao < 10**3):
                matriz_tradicional = MatrizTradicional(dimensao, dimensao)
                for _ in range(elementos_nao_nulos):
                    i, j = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
                    valor = random.randint(1, 100)
                    matriz_tradicional.inserir_atualizar(i, j, valor)

                tempo, memoria, _ = ComparadorEstruturas.medir_tempo_memoria(operacao, matriz_tradicional)
                print(f"MatrizTradicional: {tempo:.6f}s, {memoria} bytes")
                resultados[nome]["MatrizTradicional"] = (tempo, memoria)
                del matriz_tradicional 
                gc.collect()
            else:
                resultados[nome]["MatrizTradicional"] = (0.0, 0.0)

        ComparadorEstruturas.salva_csv("resultados_completos.csv", resultados, dimensao, esparsidade)

        del resultados
        gc.collect()

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