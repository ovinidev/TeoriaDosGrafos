import unittest
from grafo_adj import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adiciona_aresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adiciona_aresta(i)
        self.carga_gp = ['M', 'J']
        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adiciona_aresta(i)

        self.cargag_c = ['C', 'P']
        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')



        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adiciona_aresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adiciona_vertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adiciona_aresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adiciona_vertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adiciona_aresta(i)

        self.g_16 = Grafo([],[])
        for i in ['a', 'b', 'c', 'd', 'e']:
            self.g_16.adiciona_vertice(i)

        for i in ['a-b', 'b-c', 'b-d', 'b-e', 'c-d', 'e-c']:
            self.g_16.adiciona_aresta(i)
        self.carga_g16 = ['c']

        self.g_17 = Grafo([], [])

        for i in ['a', 'b', 'c', 'd', 'e']:
            self.g_17.adiciona_vertice(i)
        for i in ['a-e', 'b-a', 'b-e', 'b-c', 'c-a', 'c-d', 'e-d', 'e-c']:
            self.g_17.adiciona_aresta(i)

        self.g_18 = Grafo([], [])

        for i in ['a', 'b', 'c', 'd', 'e', 'f']:
            self.g_18.adiciona_vertice(i)

        for i in ['a-b', 'a-f', 'b-e', 'c-b', 'c-d', 'd-e', 'f-e']:
            self.g_18.adiciona_aresta(i)
        self.carga18 = ['d']


        self.g_19 = Grafo([], [])

        for i in ['a', 'b', 'c', 'd', 'e', 'f']:
            self.g_19.adiciona_vertice(i)

        for i in ['b-a', 'b-e', 'b-f', 'd-e', 'f-c', 'e-f']:
            self.g_19.adiciona_aresta(i)

        self.g_challenger = Grafo([], [])
        for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
            self.g_challenger.adiciona_vertice(i)
        for i in ['A-B', 'A-C', 'A-D', 'B-I', 'B-H', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B',
                  'G-J', 'H-G',
                  'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'Q-R', 'P-R', 'P-T', 'R-5',
                  'R-Y',
                  'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
                  '5-T', '5-V', '6-3', '7-6']:
            self.g_challenger.adiciona_aresta(i)
        self.lista_carga = ['L','R','U','6']

        self.c2 = Grafo([], [])

        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.c2.adiciona_vertice(i)
        for i in ['h-f', 'h-b', 'f-g', 'g-e', 'e-d', 'b-c', 'c-a', 'a-d']:
            self.c2.adiciona_aresta(i)

        self.r = ['g']
        self.n = Grafo([], [])
        for i in ['a', 'b', 'c', 'd', 'e']:
            self.n.adiciona_vertice(i)
        for i in ['a-b', 'b-c', 'c-d', 'd-e']:
            self.n.adiciona_aresta(i)
        self.carga = ['a']

    def test_dijkstra(self):
        self.assertEqual(self.g_challenger.dijkstra(3, 5, self.lista_carga, 'A', 'S'),
                             ['S', '3', '6', '7', 'U', 'T', '5', 'R', 'Q', 'M', 'L', 'E', 'D', 'A'])
        self.assertEqual(self.c2.dijkstra(2, 2, self.r, 'h', 'd'), ['d', 'e', 'g', 'f', 'h'])
        self.assertEqual(self.n.dijkstra(4, 4, self.carga, 'a', 'e'), ['e', 'd', 'c', 'b', 'a'])
        self.assertEqual(self.g_16.dijkstra(2, 3, self.carga_g16, 'a', 'e'), ['e', 'b', 'a'])
        self.assertEqual(self.g_18.dijkstra(2, 3, self.carga18, 'a', 'e'), ['e', 'b', 'a'])
        self.assertEqual(self.g_c.dijkstra(3, 3, self.cargag_c, 'E', 'J'), ['J', 'E'])
        self.assertEqual(self.g_challenger.dijkstra(5, 5, self.lista_carga, 'A', 'S'),
                             ['S', '3', '6', '7', 'U', 'T', '5', 'R', 'Q', 'M', 'L', 'E', 'D', 'A'])
        self.assertEqual(self.g_p_sem_paralelas.dijkstra(2, 2, self.carga_gp, 'C', 'Z'), ['Z', 'T', 'C'])





