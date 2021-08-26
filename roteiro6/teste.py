from meu_grafo_matriz_adjacencia_dir import *

graf_1 = MeuGrafo(['A', 'B', 'C', 'D'])

graf_1.adicionaAresta('a1', 'A', 'B')
graf_1.adicionaAresta('a2', 'B', 'C')
graf_1.adicionaAresta('a3', 'C', 'D')
graf_1.adicionaAresta('a4', 'D', 'B')

print(graf_1.warshall())

