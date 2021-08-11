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

euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
euleriano.adicionaAresta('a1', 'A', 'B')
euleriano.adicionaAresta('a2', 'B', 'D')
euleriano.adicionaAresta('a3', 'A', 'C')
euleriano.adicionaAresta('a4', 'C', 'D')
euleriano.adicionaAresta('a5', 'D', 'E')
euleriano.adicionaAresta('a6', 'D', 'F')
euleriano.adicionaAresta('a7', 'E', 'F')

print(euleriano.printEulerPathCircuit())