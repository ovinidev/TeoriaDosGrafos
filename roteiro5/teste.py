from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

# v_v = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])

# v_v.adicionaAresta('a1', 'V1', 'V2')
# v_v.adicionaAresta('a2', 'V1', 'V3')
# v_v.adicionaAresta('a3', 'V3', 'V2')
# v_v.adicionaAresta('a4', 'V3', 'V4')
# v_v.adicionaAresta('a5', 'V4', 'V5')
# v_v.adicionaAresta('a6', 'V5', 'V8')
# v_v.adicionaAresta('a7', 'V5', 'V7')
# v_v.adicionaAresta('a8', 'V6', 'V7')



g_p_dfs_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_dfs_T.adicionaAresta('a6', 'T', 'C')
g_p_dfs_T.adicionaAresta('a1', 'J', 'C')
g_p_dfs_T.adicionaAresta('a2', 'C', 'E')
g_p_dfs_T.adicionaAresta('a4', 'P', 'C')
g_p_dfs_T.adicionaAresta('a7', 'M', 'C')
g_p_dfs_T.adicionaAresta('a9', 'T', 'Z')
print(g_p_dfs_T.printEulerPathCircuit())