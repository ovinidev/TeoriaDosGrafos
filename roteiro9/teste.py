from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo
grafo = MeuGrafo(['7', '5', '3', '11', '8', '2', '9', '10'])

grafo.adicionaAresta('a1', '7', '8')
grafo.adicionaAresta('a2', '5', '8')
grafo.adicionaAresta('a3', '5', '10')
grafo.adicionaAresta('a4', '11', '10')
grafo.adicionaAresta('a5', '8', '9')
grafo.adicionaAresta('a6', '11', '9')
grafo.adicionaAresta('a7', '11', '2')
grafo.adicionaAresta('a8', '7', '11')
grafo.adicionaAresta('a9', '3', '11')


print(grafo.topologico())
print(grafo)