from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *

v_v = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
v_v.adicionaAresta('a1', 'V1', 'V2')
v_v.adicionaAresta('a2', 'V1', 'V3')
v_v.adicionaAresta('a3', 'V3', 'V2')
v_v.adicionaAresta('a4', 'V3', 'V4')
v_v.adicionaAresta('a5', 'V4', 'V5')
v_v.adicionaAresta('a6', 'V5', 'V8')
v_v.adicionaAresta('a7', 'V5', 'V7')
v_v.adicionaAresta('a8', 'V6', 'V7')

print(v_v.eh_ponte('a1'))
print(v_v.eh_ponte('a2'))
print(v_v.eh_ponte('a3'))
print(v_v.eh_ponte('a4'))
print(v_v.eh_ponte('a5'))
print(v_v.eh_ponte('a6'))
print(v_v.eh_ponte('a7'))
print(v_v.eh_ponte('a8'))
