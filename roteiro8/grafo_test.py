import unittest
from bibgrafo.grafo_exceptions import *
from meu_grafo import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C', 5)
        self.g_p.adicionaAresta('a2', 'C', 'E', 3)
        self.g_p.adicionaAresta('a3', 'C', 'E', 4)
        self.g_p.adicionaAresta('a4', 'P', 'C', 2)
        self.g_p.adicionaAresta('a5', 'P', 'C', 1)
        self.g_p.adicionaAresta('a6', 'T', 'C', 5)
        self.g_p.adicionaAresta('a7', 'M', 'C', 7)
        self.g_p.adicionaAresta('a8', 'M', 'T', 8)
        self.g_p.adicionaAresta('a9', 'T', 'Z', 9)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C', 2)
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E', 5)
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C', 3)
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C', 4)
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C', 6)
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T', 7)
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z', 10)

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C', 2)
        self.g_c.adicionaAresta('a2', 'J', 'E', 6)
        self.g_c.adicionaAresta('a3', 'J', 'P', 4)
        self.g_c.adicionaAresta('a4', 'E', 'C', 2)
        self.g_c.adicionaAresta('a5', 'P', 'C', 5)
        self.g_c.adicionaAresta('a6', 'P', 'E', 3)

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A', 5)
        self.g_l1.adicionaAresta('a2', 'A', 'B', 2)
        self.g_l1.adicionaAresta('a3', 'A', 'A', 3)

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B', 7)
        self.g_l2.adicionaAresta('a2', 'B', 'B', 5)
        self.g_l2.adicionaAresta('a3', 'B', 'A', 4)

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A', 8)
        self.g_l3.adicionaAresta('a2', 'C', 'C', 8)
        self.g_l3.adicionaAresta('a3', 'D', 'D', 7)
        self.g_l3.adicionaAresta('a4', 'D', 'D', 5)

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_v1 = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
        self.g_v1.adicionaAresta('a1', 'V1', 'V2', 3)
        self.g_v1.adicionaAresta('a2', 'V2', 'V3', 4)
        self.g_v1.adicionaAresta('a3', 'V3', 'V4', 2)
        self.g_v1.adicionaAresta('a4', 'V4', 'V5', 7)
        self.g_v1.adicionaAresta('a5', 'V5', 'V6', 8)
        self.g_v1.adicionaAresta('a6', 'V7', 'V8', 2)

        # Grafo NLW
        self.nlw = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw.adicionaAresta('1', 'A', 'B', 2)
        self.nlw.adicionaAresta('2', 'A', 'G', 4)
        self.nlw.adicionaAresta('3', 'A', 'J', 6)
        self.nlw.adicionaAresta('4', 'K', 'G', 3)
        self.nlw.adicionaAresta('5', 'K', 'J', 4)
        self.nlw.adicionaAresta('6', 'J', 'G', 2)
        self.nlw.adicionaAresta('7', 'J', 'I', 1)
        self.nlw.adicionaAresta('8', 'I', 'G', 8)
        self.nlw.adicionaAresta('9', 'G', 'H', 6)
        self.nlw.adicionaAresta('10', 'H', 'F', 7)
        self.nlw.adicionaAresta('11', 'F', 'B', 4)
        self.nlw.adicionaAresta('12', 'G', 'B', 3)
        self.nlw.adicionaAresta('13', 'B', 'C', 2)
        self.nlw.adicionaAresta('14', 'C', 'D', 7)
        self.nlw.adicionaAresta('15', 'D', 'E', 2)
        self.nlw.adicionaAresta('16', 'B', 'D', 3)
        self.nlw.adicionaAresta('17', 'B', 'E', 5)

        self.grafo_roteiro = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo_roteiro.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo_roteiro.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo_roteiro.adicionaAresta('a3', 'C', 'G', 2)
        self.grafo_roteiro.adicionaAresta('a4', 'G', 'F', 3)
        self.grafo_roteiro.adicionaAresta('a5', 'E', 'F', 4)
        self.grafo_roteiro.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo_roteiro.adicionaAresta('a7', 'E', 'D', 2)
        self.grafo_roteiro.adicionaAresta('a8', 'A', 'D', 3)
        self.grafo_roteiro.adicionaAresta('a9', 'B', 'G', 5)
        self.grafo_roteiro.adicionaAresta('a10', 'D', 'G', 3)

        self.graph1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.graph1.adicionaAresta('a1', 'A', 'B', 7)
        self.graph1.adicionaAresta('a2', 'B', 'C', 8)
        self.graph1.adicionaAresta('a3', 'C', 'E', 5)
        self.graph1.adicionaAresta('a4', 'E', 'G', 9)
        self.graph1.adicionaAresta('a5', 'G', 'F', 11)
        self.graph1.adicionaAresta('a6', 'F', 'D', 6)
        self.graph1.adicionaAresta('a7', 'D', 'A', 5)
        self.graph1.adicionaAresta('a8', 'D', 'E', 15)
        self.graph1.adicionaAresta('a9', 'B', 'E', 7)
        self.graph1.adicionaAresta('a10', 'B', 'D', 9)

        # Eureliano

        self.euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.euleriano.adicionaAresta('a1', 'A', 'B', 7)
        self.euleriano.adicionaAresta('a2', 'B', 'D', 5)
        self.euleriano.adicionaAresta('a3', 'A', 'C', 2)
        self.euleriano.adicionaAresta('a4', 'C', 'D', 8)
        self.euleriano.adicionaAresta('a5', 'D', 'E', 5)
        self.euleriano.adicionaAresta('a6', 'D', 'F', 6)
        self.euleriano.adicionaAresta('a7', 'E', 'F', 2)

        self.semi_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.semi_euleriano.adicionaAresta('a1', 'A', 'B', 23)
        self.semi_euleriano.adicionaAresta('a2', 'A', 'C', 20)
        self.semi_euleriano.adicionaAresta('a3', 'A', 'E', 18)
        self.semi_euleriano.adicionaAresta('a4', 'B', 'E', 23)
        self.semi_euleriano.adicionaAresta('a5', 'C', 'E', 24)
        self.semi_euleriano.adicionaAresta('a6', 'D', 'E', 23)
        self.semi_euleriano.adicionaAresta('a7', 'B', 'D', 22)
        self.semi_euleriano.adicionaAresta('a8', 'C', 'D', 20)
        self.semi_euleriano.adicionaAresta('a9', 'C', 'F', 15)
        self.semi_euleriano.adicionaAresta('a10', 'D', 'F', 10)

        self.v_v = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])

        self.v_v.adicionaAresta('a1', 'V1', 'V2', 2)
        self.v_v.adicionaAresta('a2', 'V1', 'V3', 7)
        self.v_v.adicionaAresta('a3', 'V3', 'V2', 3)
        self.v_v.adicionaAresta('a4', 'V3', 'V4', 5)
        self.v_v.adicionaAresta('a5', 'V4', 'V5', 4)
        self.v_v.adicionaAresta('a6', 'V5', 'V8', 1)
        self.v_v.adicionaAresta('a7', 'V5', 'V7', 6)
        self.v_v.adicionaAresta('a8', 'V6', 'V7', 3)

        # Não Eureliano

        self.nao_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E'])

        self.nao_euleriano.adicionaAresta('a1', 'A', 'B', 7)
        self.nao_euleriano.adicionaAresta('a2', 'A', 'C', 1)
        self.nao_euleriano.adicionaAresta('a3', 'A', 'E', 2)
        self.nao_euleriano.adicionaAresta('a4', 'B', 'E', 3)
        self.nao_euleriano.adicionaAresta('a5', 'C', 'E', 5)
        self.nao_euleriano.adicionaAresta('a6', 'D', 'E', 6)
        self.nao_euleriano.adicionaAresta('a7', 'B', 'D', 8)
        self.nao_euleriano.adicionaAresta('a8', 'C', 'D', 6)

        #Arvore Prim

        self.nlw_prim = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_prim.adicionaAresta('7', 'J', 'I', 1)
        self.nlw_prim.adicionaAresta('6', 'J', 'G', 2)
        self.nlw_prim.adicionaAresta('4', 'K', 'G', 3)
        self.nlw_prim.adicionaAresta('12', 'G', 'B', 3)
        self.nlw_prim.adicionaAresta('1', 'A', 'B', 2)
        self.nlw_prim.adicionaAresta('13', 'B', 'C', 2)
        self.nlw_prim.adicionaAresta('16', 'B', 'D', 3)
        self.nlw_prim.adicionaAresta('15', 'D', 'E', 2)
        self.nlw_prim.adicionaAresta('11', 'F', 'B', 4)
        self.nlw_prim.adicionaAresta('9', 'G', 'H', 6)

        self.grafo_roteiro_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo_roteiro_prim.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo_roteiro_prim.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo_roteiro_prim.adicionaAresta('a3', 'C', 'G', 2)
        self.grafo_roteiro_prim.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo_roteiro_prim.adicionaAresta('a7', 'E', 'D', 2)
        self.grafo_roteiro_prim.adicionaAresta('a4', 'G', 'F', 3)

        self.graph1_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.graph1_prim.adicionaAresta('a1', 'A', 'B', 7)
        self.graph1_prim.adicionaAresta('a3', 'C', 'E', 5)
        self.graph1_prim.adicionaAresta('a4', 'E', 'G', 9)
        self.graph1_prim.adicionaAresta('a6', 'F', 'D', 6)
        self.graph1_prim.adicionaAresta('a7', 'D', 'A', 5)
        self.graph1_prim.adicionaAresta('a9', 'B', 'E', 7)

        self.g_p_prim = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_prim.adicionaAresta('a1', 'J', 'C', 5)
        self.g_p_prim.adicionaAresta('a2', 'C', 'E', 3)
        self.g_p_prim.adicionaAresta('a5', 'P', 'C', 1)
        self.g_p_prim.adicionaAresta('a6', 'T', 'C', 5)
        self.g_p_prim.adicionaAresta('a7', 'M', 'C', 7)
        self.g_p_prim.adicionaAresta('a9', 'T', 'Z', 9)

        self.g_p_sem_paralelas_prim = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_prim.adicionaAresta('a1', 'J', 'C', 2)
        self.g_p_sem_paralelas_prim.adicionaAresta('a2', 'C', 'E', 5)
        self.g_p_sem_paralelas_prim.adicionaAresta('a3', 'P', 'C', 3)
        self.g_p_sem_paralelas_prim.adicionaAresta('a4', 'T', 'C', 4)
        self.g_p_sem_paralelas_prim.adicionaAresta('a5', 'M', 'C', 6)
        self.g_p_sem_paralelas_prim.adicionaAresta('a7', 'T', 'Z', 10)

        self.g_c_prim = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_prim.adicionaAresta('a1','J','C', 2)
        self.g_c_prim.adicionaAresta('a4', 'E', 'C', 2)
        self.g_c_prim.adicionaAresta('a6', 'P', 'E', 3)

        self.euleriano_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.euleriano_prim.adicionaAresta('a1', 'A', 'B', 7)
        self.euleriano_prim.adicionaAresta('a2', 'B', 'D', 5)
        self.euleriano_prim.adicionaAresta('a3', 'A', 'C', 2)
        self.euleriano_prim.adicionaAresta('a5', 'D', 'E', 5)
        self.euleriano_prim.adicionaAresta('a7', 'E', 'F', 2)

        self.semi_euleriano_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.semi_euleriano_prim.adicionaAresta('a2', 'A', 'C', 20)
        self.semi_euleriano_prim.adicionaAresta('a3', 'A', 'E', 18)
        self.semi_euleriano_prim.adicionaAresta('a7', 'B', 'D', 22)
        self.semi_euleriano_prim.adicionaAresta('a9', 'C', 'F', 15)
        self.semi_euleriano_prim.adicionaAresta('a10', 'D', 'F', 10)

        #Arvore Kruskal

        self.g_p_kruskal = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_kruskal.adicionaAresta('a1', 'J', 'C', 5)
        self.g_p_kruskal.adicionaAresta('a2', 'C', 'E', 3)
        self.g_p_kruskal.adicionaAresta('a5', 'P', 'C', 1)
        self.g_p_kruskal.adicionaAresta('a6', 'T', 'C', 5)
        self.g_p_kruskal.adicionaAresta('a7', 'M', 'C', 7)
        self.g_p_kruskal.adicionaAresta('a9', 'T', 'Z', 9)

        self.g_c_kruskal = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c_kruskal.adicionaAresta('a1','J','C', 2)
        self.g_c_kruskal.adicionaAresta('a4', 'E', 'C', 2)
        self.g_c_kruskal.adicionaAresta('a6', 'P', 'E', 3)

        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C', 2)
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C', 3)
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C', 4)
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C', 6)
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z', 10)

        self.nlw_kruskal = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_kruskal.adicionaAresta('1', 'A', 'B', 2)
        self.nlw_kruskal.adicionaAresta('4', 'K', 'G', 3)
        self.nlw_kruskal.adicionaAresta('6', 'J', 'G', 2)
        self.nlw_kruskal.adicionaAresta('7', 'J', 'I', 1)
        self.nlw_kruskal.adicionaAresta('9', 'G', 'H', 6)
        self.nlw_kruskal.adicionaAresta('11', 'F', 'B', 4)
        self.nlw_kruskal.adicionaAresta('12', 'G', 'B', 3)
        self.nlw_kruskal.adicionaAresta('13', 'B', 'C', 2)
        self.nlw_kruskal.adicionaAresta('15', 'D', 'E', 2)
        self.nlw_kruskal.adicionaAresta('16', 'B', 'D', 3)

        self.grafo_roteiro_kruskal = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo_roteiro_kruskal.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo_roteiro_kruskal.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo_roteiro_kruskal.adicionaAresta('a3', 'C', 'G', 2)
        self.grafo_roteiro_kruskal.adicionaAresta('a4', 'G', 'F', 3)
        self.grafo_roteiro_kruskal.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo_roteiro_kruskal.adicionaAresta('a7', 'E', 'D', 2)

        self.graph1_kruskal = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.graph1_kruskal.adicionaAresta('a1', 'A', 'B', 7)
        self.graph1_kruskal.adicionaAresta('a3', 'C', 'E', 5)
        self.graph1_kruskal.adicionaAresta('a4', 'E', 'G', 9)
        self.graph1_kruskal.adicionaAresta('a6', 'F', 'D', 6)
        self.graph1_kruskal.adicionaAresta('a7', 'D', 'A', 5)
        self.graph1_kruskal.adicionaAresta('a9', 'B', 'E', 7)

        self.euleriano_kruskal = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.euleriano_kruskal.adicionaAresta('a1', 'A', 'B', 7)
        self.euleriano_kruskal.adicionaAresta('a3', 'A', 'C', 2)
        self.euleriano_kruskal.adicionaAresta('a5', 'D', 'E', 5)
        self.euleriano_kruskal.adicionaAresta('a2', 'D', 'B', 5)
        self.euleriano_kruskal.adicionaAresta('a7', 'E', 'F', 2)

        self.semi_euleriano_kruskal = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.semi_euleriano_kruskal.adicionaAresta('a2', 'A', 'C', 20)
        self.semi_euleriano_kruskal.adicionaAresta('a3', 'A', 'E', 18)
        self.semi_euleriano_kruskal.adicionaAresta('a7', 'B', 'D', 22)
        self.semi_euleriano_kruskal.adicionaAresta('a9', 'C', 'F', 15)
        self.semi_euleriano_kruskal.adicionaAresta('a10', 'D', 'F', 10)

        self.v_v_kruskal = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
        self.v_v_kruskal.adicionaAresta('a1', 'V1', 'V2', 2)
        self.v_v_kruskal.adicionaAresta('a3', 'V3', 'V2', 3)
        self.v_v_kruskal.adicionaAresta('a4', 'V3', 'V4', 5)
        self.v_v_kruskal.adicionaAresta('a5', 'V4', 'V5', 4)
        self.v_v_kruskal.adicionaAresta('a6', 'V5', 'V8', 1)
        self.v_v_kruskal.adicionaAresta('a7', 'V5', 'V7', 6)
        self.v_v_kruskal.adicionaAresta('a8', 'V6', 'V7', 3)


        self.nao_euleriano_kruskal = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.nao_euleriano_kruskal.adicionaAresta('a2', 'A', 'C', 1)
        self.nao_euleriano_kruskal.adicionaAresta('a3', 'A', 'E', 2)
        self.nao_euleriano_kruskal.adicionaAresta('a4', 'B', 'E', 3)
        self.nao_euleriano_kruskal.adicionaAresta('a6', 'D', 'E', 6)

    def test_prim(self):
        self.assertEqual(self.nlw.prim(), self.nlw_prim)
        self.assertEqual(self.grafo_roteiro.prim(), self.grafo_roteiro_prim)
        self.assertEqual(self.graph1.prim(), self.graph1_prim)
        self.assertEqual(self.g_p.prim(), self.g_p_prim)
        self.assertEqual(self.g_c.prim(), self.g_c_prim)
        self.assertFalse(self.g_l1.prim())
        self.assertFalse(self.g_l2.prim())
        self.assertFalse(self.g_l3.prim())
        self.assertEqual(self.euleriano.prim(), self.euleriano_prim)
        self.assertEqual(self.semi_euleriano.prim(), self.semi_euleriano_prim)
        
    def test_kruskal(self):
        self.assertEqual(self.g_p.kruskal(), self.g_p_kruskal)
        self.assertEqual(self.g_c.kruskal(), self.g_c_kruskal)
        self.assertEqual(self.nlw.kruskal(), self.nlw_kruskal)
        self.assertEqual(self.grafo_roteiro.kruskal(), self.grafo_roteiro_kruskal)
        self.assertEqual(self.graph1.kruskal(), self.graph1_kruskal)
        self.assertEqual(self.euleriano.kruskal(), self.euleriano_kruskal)
        self.assertEqual(self.euleriano.kruskal(), self.euleriano_kruskal)
        self.assertEqual(self.semi_euleriano.kruskal(), self.semi_euleriano_kruskal)
        self.assertEqual(self.v_v.kruskal(), self.v_v_kruskal)
        self.assertEqual(self.nao_euleriano.kruskal(), self.nao_euleriano_kruskal)

