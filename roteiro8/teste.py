from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *




nao_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E'])

nao_euleriano.adicionaAresta('a1', 'A', 'B', 7)
nao_euleriano.adicionaAresta('a2', 'A', 'C', 1)
nao_euleriano.adicionaAresta('a3', 'A', 'E', 2)
nao_euleriano.adicionaAresta('a4', 'B', 'E', 3)
nao_euleriano.adicionaAresta('a5', 'C', 'E', 5)
nao_euleriano.adicionaAresta('a6', 'D', 'E', 6)
nao_euleriano.adicionaAresta('a7', 'B', 'D', 8)
nao_euleriano.adicionaAresta('a8', 'C', 'D', 6)

print(nao_euleriano.kruskal())