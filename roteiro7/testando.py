from grafo_adj import Grafo
from math import inf
g_challenger = Grafo([], [])
for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
    g_challenger.adiciona_vertice(i)
for i in ['A-B','A-C', 'A-D', 'B-I','B-H', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B', 'G-J', 'H-G',
           'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'Q-R','P-R', 'P-T', 'R-5', 'R-Y',
          'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
           '5-T', '5-V', '6-3', '7-6']:
    g_challenger.adiciona_aresta(i)

lista_carga = ['L','R','U','6']


n = Grafo([], [])
for i in ['a','b','c','d','e']:
    n.adiciona_vertice(i)
for i in ['a-b','b-c','c-d','d-e']:
    n.adiciona_aresta(i)
l = ['a']
print(n.dijkstra(4,4,l,'a','e'))
c2 = Grafo([], [])

for i in ['a','b','c','d','e','f','g','h']:
    c2.adiciona_vertice(i)
for i in ['h-f','h-b','f-g','g-e','e-d','b-c','c-a','a-d']:
    c2.adiciona_aresta(i)

r = ['g']

#print(c2.dijkstra(2,2,r,'h','d'))
#g_challenger.dijkstra('A','J')
#print(g_challenger.dijkstra(3, 5,lista_carga, 'A','S'))

g_18 = Grafo([], [])

for i in ['a', 'b', 'c', 'd', 'e', 'f']:
     g_18.adiciona_vertice(i)

for i in ['a-b', 'a-f', 'b-e', 'c-b', 'c-d', 'd-e', 'f-e']:
    g_18.adiciona_aresta(i)


carga = ['d']
print(g_18.dijkstra(2, 3, carga, 'a', 'e'))


g_c = Grafo([], [])
for i in ['J', 'C', 'E', 'P']:
    g_c.adiciona_vertice(i)
for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
    g_c.adiciona_aresta(i)

carga_c = ['C', 'P']
print(g_c.dijkstra(3, 3, carga_c, 'E', 'J'))
g_p_sem_paralelas = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p_sem_paralelas.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p_sem_paralelas.adiciona_aresta(i)
carga_gp = ['M', 'J']
print(g_p_sem_paralelas.dijkstra(2, 2, carga_gp, 'C', 'Z'))

g_16 = Grafo([],[])
for i in ['a', 'b', 'c', 'd', 'e']:
    g_16.adiciona_vertice(i)

for i in ['a-b', 'b-c', 'b-d', 'b-e', 'c-d', 'e-c']:
    g_16.adiciona_aresta(i)
carga_g16 = ['c']
print(g_16.dijkstra(2, 3, carga_g16, 'a', 'e'))


