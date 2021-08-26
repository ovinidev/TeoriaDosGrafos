from meu_grafo_matriz_adjacencia_dir import *

g_v1 = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
g_v1.adicionaAresta('a1', 'V1', 'V2')
g_v1.adicionaAresta('a2', 'V2', 'V3')
g_v1.adicionaAresta('a3', 'V3', 'V4')
g_v1.adicionaAresta('a4', 'V4', 'V5')
g_v1.adicionaAresta('a5', 'V5', 'V6')
g_v1.adicionaAresta('a6', 'V7', 'V8')

print(g_v1.warshall())

