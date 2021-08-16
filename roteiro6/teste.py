from meu_grafo_matriz_adjacencia_dir import *

grafo = MeuGrafo(['A', 'B', 'C', 'D'])

grafo.adicionaAresta('a1', 'A', 'B')
grafo.adicionaAresta('a2', 'B', 'C')
grafo.adicionaAresta('a3', 'C', 'D')
grafo.adicionaAresta('a4', 'D', 'B')

print(grafo.warshall())