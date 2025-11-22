# Tipos abstratos de dados para representação de matrizes esparsas

## Descrição do Projeto
Este projeto implementa e compara diferentes estruturas de dados para representar matrizes esparsas e tradicionais. Ele inclui ferramentas para gerar matrizes, realizar operações matemáticas e medir o desempenho (tempo e memória) de cada estrutura.

## Disciplina
MC 458 - 2º semestre de 2025

## Autores
- Gustavo Eugenio John — RA 248318
- Lucas Cardoso Pereira — RA 281817
- Lucca Maso Miranda — RA 281827

## Estruturas e Arquivos

- **`estrutura_um.py`**: Implementa a Estrutura 1, que utiliza uma abordagem de dicionários aninhados (com a implementação nativa do Python 3 para dicionários) para representar matrizes esparsas. A classe mantém dois atributos principais: `linha` e `linha_t` (para a transposta). No atributo `linha`, as chaves do dicionário representam os índices das linhas, e cada chave mapeia para um dicionário interno onde as chaves representam os índices das colunas e os valores armazenam o elemento da matriz. O atributo `linha_t` segue o mesmo princípio, mas com as linhas e colunas invertidas. Essa estrutura garante complexidade esperada de O(1) para acesso em caso médio.

- **`estrutura_dois.py`**: Implementa a Estrutura 2, que utiliza árvores AVL para representar matrizes esparsas. A classe mantém dois atributos principais: `linhas` e `colunas` (para a transposta). No atributo `linhas`, a árvore externa utiliza os índices das linhas como chaves de busca, e cada linha com elementos não nulos é representada como um nó cuja informação associada é outra árvore AVL interna. Essa árvore interna armazena os índices das colunas como chaves e os valores dos elementos como dados. O atributo `colunas` implementa a mesma estratégia, mas com as linhas e colunas invertidas. Ambas as buscas operam em tempo logarítmico.

- **`matriz_tradicional.py`**: Implementa a Matriz Tradicional, que utiliza uma lista de listas para armazenar todos os elementos, inclusive os zeros. Essa implementação não explora esparsidade, mas foi incluída no projeto para fins de comparação com as demais estruturas esparsas. Ela serve como referência de desempenho e consumo de memória em relação às abordagens otimizadas.

- **`gerador_matrizes.py`**: Contém funções para gerar matrizes esparsas e densas com diferentes dimensões e níveis de esparsidade.

- **`comparador_estruturas.py`**: Compara o desempenho das estruturas em várias operações, como soma, multiplicação e transposição de matrizes. Salva os resultados em um arquivo CSV para análise posterior.

- **`arvore_avl.py`**: Contém a implementação da árvore AVL utilizada pela Estrutura 2. A árvore AVL é uma estrutura de dados balanceada que garante que as operações de inserção, remoção e busca sejam realizadas em tempo logarítmico. Essa implementação é usada para armazenar e organizar os índices das linhas e colunas das matrizes esparsas de forma eficiente.

## Como Executar
1. Certifique-se de que todas as dependências estão instaladas (se necessário).
2. Execute o arquivo `main.py`:
   ```bash
   python3 main.py
   ```

Os resultados serão salvos em um arquivo CSV chamado `resultados_completos.csv`.

## Estrutura do CSV
O arquivo CSV gerado contém as seguintes informações:
- Dimensão da matriz
- Esparsidade
- Operação realizada
- Tempo e memória utilizados por cada estrutura
