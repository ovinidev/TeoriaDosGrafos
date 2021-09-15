from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

grafo_roteiro = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafo_roteiro.adicionaAresta('a1', 'A', 'B', 1)
grafo_roteiro.adicionaAresta('a2', 'B', 'C', 2)
grafo_roteiro.adicionaAresta('a3', 'C', 'G', 2)
grafo_roteiro.adicionaAresta('a4', 'G', 'F', 3)
grafo_roteiro.adicionaAresta('a5', 'E', 'F', 4)
grafo_roteiro.adicionaAresta('a6', 'E', 'G', 1)
grafo_roteiro.adicionaAresta('a7', 'E', 'D', 2)
grafo_roteiro.adicionaAresta('a8', 'A', 'D', 3)
grafo_roteiro.adicionaAresta('a9', 'B', 'G', 5)
grafo_roteiro.adicionaAresta('a10', 'D', 'G', 3)
print(grafo_roteiro.prim())
