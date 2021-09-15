from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C', 5)
g_p.adicionaAresta('a2', 'C', 'E', 3)
g_p.adicionaAresta('a3', 'C', 'E', 4)
g_p.adicionaAresta('a4', 'P', 'C', 2)
g_p.adicionaAresta('a5', 'P', 'C', 1)
g_p.adicionaAresta('a6', 'T', 'C', 5)
g_p.adicionaAresta('a7', 'M', 'C', 7)
g_p.adicionaAresta('a8', 'M', 'T', 8)
g_p.adicionaAresta('a9', 'T', 'Z', 9)

print(g_p.prim())