from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
g_l1.adicionaAresta('a3', 'A', 'A')

print(g_l1.ha_ciclo())