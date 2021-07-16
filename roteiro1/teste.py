from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *


nlw = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])


nlw.adicionaAresta('1', 'A', 'B')
nlw.adicionaAresta('2', 'A', 'G')
nlw.adicionaAresta('3', 'A', 'J')
nlw.adicionaAresta('4', 'K', 'G')
nlw.adicionaAresta('5', 'K', 'J')
nlw.adicionaAresta('6', 'J', 'G')
nlw.adicionaAresta('7', 'J', 'I')
nlw.adicionaAresta('8', 'I', 'G')
nlw.adicionaAresta('9', 'G', 'H')
nlw.adicionaAresta('10', 'H', 'F')
nlw.adicionaAresta('11', 'F', 'B')
nlw.adicionaAresta('12', 'G', 'B')
nlw.adicionaAresta('13', 'B', 'C')
nlw.adicionaAresta('14', 'C', 'D')
nlw.adicionaAresta('15', 'D', 'E')
nlw.adicionaAresta('16', 'B', 'D')
nlw.adicionaAresta('17', 'B', 'E')

print("nlw", nlw.dfs("C"))
