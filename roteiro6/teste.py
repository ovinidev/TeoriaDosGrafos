from meu_grafo_matriz_adjacencia_dir import *

grafo = MeuGrafo(['A', 'B', 'C', 'D'])

grafo.adicionaAresta('a1', 'A', 'B')
grafo.adicionaAresta('a2', 'A', 'C')
grafo.adicionaAresta('a3', 'B', 'C')
grafo.adicionaAresta('a4', 'C', 'D')
grafo.adicionaAresta('a5', 'C', 'A')

print(grafo.warshall())