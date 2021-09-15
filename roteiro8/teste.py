from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *



semi_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
semi_euleriano.adicionaAresta('a1', 'A', 'B', 23)
semi_euleriano.adicionaAresta('a2', 'A', 'C', 20)
semi_euleriano.adicionaAresta('a3', 'A', 'E', 18)
semi_euleriano.adicionaAresta('a4', 'B', 'E', 23)
semi_euleriano.adicionaAresta('a5', 'C', 'E', 24)
semi_euleriano.adicionaAresta('a6', 'D', 'E', 23)
semi_euleriano.adicionaAresta('a7', 'B', 'D', 22)
semi_euleriano.adicionaAresta('a8', 'C', 'D', 20)
semi_euleriano.adicionaAresta('a9', 'C', 'F', 15)
semi_euleriano.adicionaAresta('a10', 'D', 'F', 10)

print(semi_euleriano.prim())