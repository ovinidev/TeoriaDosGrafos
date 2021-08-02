from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_matriz_adjacencia_nao_dir import *

g_p_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_dfs_J.adicionaAresta('a1', 'J', 'C')
g_p_dfs_J.adicionaAresta('a2', 'C', 'E')
g_p_dfs_J.adicionaAresta('a4', 'P', 'C')
g_p_dfs_J.adicionaAresta('a6', 'T', 'C')
g_p_dfs_J.adicionaAresta('a8', 'M', 'T')
g_p_dfs_J.adicionaAresta('a9', 'T', 'Z')

print(g_p_dfs_J)

