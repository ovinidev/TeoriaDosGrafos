import unittest
from bibgrafo.grafo_exceptions import *
from meu_grafo_matriz_adjacencia_dir import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba DFS
        self.g_p_dfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_dfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dfs_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_C.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_C.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_C.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_C.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_C.adicionaAresta('a8', 'M', 'T')
        self.g_p_dfs_C.adicionaAresta('a9', 'T', 'Z')

        self.g_p_dfs_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_Z.adicionaAresta('a9', 'T', 'Z')
        self.g_p_dfs_Z.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_Z.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_Z.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_Z.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_Z.adicionaAresta('a7', 'M', 'C')

        self.g_p_dfs_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_T.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_T.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_T.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_T.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_T.adicionaAresta('a7', 'M', 'C')
        self.g_p_dfs_T.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba BFS
        self.g_p_bfs_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_J.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_J.adicionaAresta('a9', 'T', 'Z')

        self.g_p_bfs_T = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_T.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_T.adicionaAresta('a8', 'M', 'T')
        self.g_p_bfs_T.adicionaAresta('a9', 'T', 'Z')
        self.g_p_bfs_T.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_T.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_T.adicionaAresta('a4', 'P', 'C')

        self.g_p_bfs_Z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_Z.adicionaAresta('a9', 'T', 'Z')
        self.g_p_bfs_Z.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_Z.adicionaAresta('a8', 'M', 'T')
        self.g_p_bfs_Z.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_Z.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_Z.adicionaAresta('a4', 'P', 'C')

        self.g_p_bfs_P = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_P.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_P.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_P.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_P.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_P.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_P.adicionaAresta('a9', 'T', 'Z')

        # Grafos direcionados

        self.graf_1 = MeuGrafo(['A', 'B', 'C', 'D'])

        self.graf_1.adicionaAresta('a1', 'A', 'B')
        self.graf_1.adicionaAresta('a2', 'B', 'C')
        self.graf_1.adicionaAresta('a3', 'C', 'D')
        self.graf_1.adicionaAresta('a4', 'D', 'B')

        self.graf_2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.graf_2.adicionaAresta('a1', 'A', 'B')
        self.graf_2.adicionaAresta('a2', 'B', 'C')
        self.graf_2.adicionaAresta('a3', 'C', 'F')
        self.graf_2.adicionaAresta('a4', 'E', 'D')
        self.graf_2.adicionaAresta('a5', 'F', 'E')
        self.graf_2.adicionaAresta('a6', 'F', 'A')
        self.graf_2.adicionaAresta('a7', 'D', 'C')

        self.graf_3 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])

        self.graf_3.adicionaAresta('a1', 'A', 'B')
        self.graf_3.adicionaAresta('a2', 'B', 'C')
        self.graf_3.adicionaAresta('a3', 'C', 'D')
        self.graf_3.adicionaAresta('a4', 'D', 'E')
        self.graf_3.adicionaAresta('a5', 'E', 'A')
        self.graf_3.adicionaAresta('a6', 'D', 'A')

        self.graf_4 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

        self.graf_4.adicionaAresta('a1', 'A', 'B')
        self.graf_4.adicionaAresta('a2', 'B', 'C')
        self.graf_4.adicionaAresta('a3', 'C', 'D')
        self.graf_4.adicionaAresta('a4', 'D', 'E')
        self.graf_4.adicionaAresta('a5', 'E', 'A')
        self.graf_4.adicionaAresta('a6', 'D', 'A')
        self.graf_4.adicionaAresta('a7', 'F', 'C')
        self.graf_4.adicionaAresta('a8', 'A', 'F')
        self.graf_4.adicionaAresta('a9', 'B', 'G')
        self.graf_4.adicionaAresta('a10', 'G', 'C')

        self.grafo_5 = MeuGrafo(['A', 'B', 'C', 'D'])

        self.grafo_5.adicionaAresta('a1', 'A', 'B')
        self.grafo_5.adicionaAresta('a2', 'A', 'C')
        self.grafo_5.adicionaAresta('a3', 'B', 'C')
        self.grafo_5.adicionaAresta('a4', 'C', 'D')
        self.grafo_5.adicionaAresta('a5', 'C', 'A')


        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_v1 = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
        self.g_v1.adicionaAresta('a1', 'V1', 'V2')
        self.g_v1.adicionaAresta('a2', 'V2', 'V3')
        self.g_v1.adicionaAresta('a3', 'V3', 'V4')
        self.g_v1.adicionaAresta('a4', 'V4', 'V5')
        self.g_v1.adicionaAresta('a5', 'V5', 'V6')
        self.g_v1.adicionaAresta('a6', 'V7', 'V8')

        # Grafo NLW
        self.nlw = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw.adicionaAresta('1', 'A', 'B')
        self.nlw.adicionaAresta('2', 'A', 'G')
        self.nlw.adicionaAresta('3', 'A', 'J')
        self.nlw.adicionaAresta('4', 'K', 'G')
        self.nlw.adicionaAresta('5', 'K', 'J')
        self.nlw.adicionaAresta('6', 'J', 'G')
        self.nlw.adicionaAresta('7', 'J', 'I')
        self.nlw.adicionaAresta('8', 'I', 'G')
        self.nlw.adicionaAresta('9', 'G', 'H')
        self.nlw.adicionaAresta('10', 'H', 'F')
        self.nlw.adicionaAresta('11', 'F', 'B')
        self.nlw.adicionaAresta('12', 'G', 'B')
        self.nlw.adicionaAresta('13', 'B', 'C')
        self.nlw.adicionaAresta('14', 'C', 'D')
        self.nlw.adicionaAresta('15', 'D', 'E')
        self.nlw.adicionaAresta('16', 'B', 'D')
        self.nlw.adicionaAresta('17', 'B', 'E')

        #Arvore DFS

        self.nlw_dfs_A = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_dfs_A.adicionaAresta('1', 'A', 'B')
        self.nlw_dfs_A.adicionaAresta('11', 'B', 'F')
        self.nlw_dfs_A.adicionaAresta('10', 'F', 'H')
        self.nlw_dfs_A.adicionaAresta('9', 'H', 'G')
        self.nlw_dfs_A.adicionaAresta('4', 'G', 'K')
        self.nlw_dfs_A.adicionaAresta('5', 'K', 'J')
        self.nlw_dfs_A.adicionaAresta('7', 'J', 'I')
        self.nlw_dfs_A.adicionaAresta('13', 'B', 'C')
        self.nlw_dfs_A.adicionaAresta('14', 'C', 'D')
        self.nlw_dfs_A.adicionaAresta('15', 'D', 'E')

        self.nlw_dfs_F = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_dfs_F.adicionaAresta('10', 'F', 'H')
        self.nlw_dfs_F.adicionaAresta('9', 'H', 'G')
        self.nlw_dfs_F.adicionaAresta('2', 'G', 'A')
        self.nlw_dfs_F.adicionaAresta('1', 'A', 'B')
        self.nlw_dfs_F.adicionaAresta('13', 'B', 'C')
        self.nlw_dfs_F.adicionaAresta('14', 'C', 'D')
        self.nlw_dfs_F.adicionaAresta('15', 'D', 'E')
        self.nlw_dfs_F.adicionaAresta('3', 'A', 'J')
        self.nlw_dfs_F.adicionaAresta('5', 'J', 'K')
        self.nlw_dfs_F.adicionaAresta('7', 'J', 'I')

        self.nlw_dfs_K = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_dfs_K.adicionaAresta('4', 'K', 'G')
        self.nlw_dfs_K.adicionaAresta('2', 'G', 'A')
        self.nlw_dfs_K.adicionaAresta('1', 'A', 'B')
        self.nlw_dfs_K.adicionaAresta('11', 'B', 'F')
        self.nlw_dfs_K.adicionaAresta('10', 'F', 'H')
        self.nlw_dfs_K.adicionaAresta('13', 'B', 'C')
        self.nlw_dfs_K.adicionaAresta('14', 'C', 'D')
        self.nlw_dfs_K.adicionaAresta('15', 'D', 'E')
        self.nlw_dfs_K.adicionaAresta('3', 'A', 'J')
        self.nlw_dfs_K.adicionaAresta('7', 'J', 'I')
       
        self.nlw_dfs_C = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_dfs_C.adicionaAresta('13', 'C', 'B')
        self.nlw_dfs_C.adicionaAresta('1', 'B', 'A')
        self.nlw_dfs_C.adicionaAresta('2', 'A', 'G')
        self.nlw_dfs_C.adicionaAresta('4', 'G', 'K')
        self.nlw_dfs_C.adicionaAresta('5', 'K', 'J')
        self.nlw_dfs_C.adicionaAresta('7', 'J', 'I')
        self.nlw_dfs_C.adicionaAresta('9', 'G', 'H')
        self.nlw_dfs_C.adicionaAresta('10', 'H', 'F')
        self.nlw_dfs_C.adicionaAresta('16', 'B', 'D')
        self.nlw_dfs_C.adicionaAresta('15', 'D', 'E')

        #Arvore BFS

        self.nlw_bfs_A = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_bfs_A.adicionaAresta('1', 'A', 'B')
        self.nlw_bfs_A.adicionaAresta('2', 'A', 'G')
        self.nlw_bfs_A.adicionaAresta('3', 'A', 'J')
        self.nlw_bfs_A.adicionaAresta('11', 'F', 'B')
        self.nlw_bfs_A.adicionaAresta('13', 'B', 'C')
        self.nlw_bfs_A.adicionaAresta('16', 'B', 'D')
        self.nlw_bfs_A.adicionaAresta('17', 'B', 'E')
        self.nlw_bfs_A.adicionaAresta('4', 'K', 'G')
        self.nlw_bfs_A.adicionaAresta('8', 'I', 'G')
        self.nlw_bfs_A.adicionaAresta('9', 'G', 'H')

        self.nlw_bfs_F = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_bfs_F.adicionaAresta('10', 'H', 'F')
        self.nlw_bfs_F.adicionaAresta('11', 'F', 'B')
        self.nlw_bfs_F.adicionaAresta('9', 'G', 'H')
        self.nlw_bfs_F.adicionaAresta('1', 'A', 'B')
        self.nlw_bfs_F.adicionaAresta('13', 'B', 'C')
        self.nlw_bfs_F.adicionaAresta('16', 'B', 'D')
        self.nlw_bfs_F.adicionaAresta('17', 'B', 'E')
        self.nlw_bfs_F.adicionaAresta('4', 'K', 'G')
        self.nlw_bfs_F.adicionaAresta('6', 'J', 'G')
        self.nlw_bfs_F.adicionaAresta('8', 'I', 'G')

        self.nlw_bfs_K = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_bfs_K.adicionaAresta('4', 'K', 'G')
        self.nlw_bfs_K.adicionaAresta('5', 'K', 'J')
        self.nlw_bfs_K.adicionaAresta('2', 'A', 'G')
        self.nlw_bfs_K.adicionaAresta('8', 'I', 'G')
        self.nlw_bfs_K.adicionaAresta('9', 'G', 'H')
        self.nlw_bfs_K.adicionaAresta('12', 'G', 'B')
        self.nlw_bfs_K.adicionaAresta('10', 'H', 'F')
        self.nlw_bfs_K.adicionaAresta('13', 'B', 'C')
        self.nlw_bfs_K.adicionaAresta('16', 'B', 'D')
        self.nlw_bfs_K.adicionaAresta('17', 'B', 'E')

        self.nlw_bfs_C = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw_bfs_C.adicionaAresta('13', 'B', 'C')
        self.nlw_bfs_C.adicionaAresta('14', 'C', 'D')
        self.nlw_bfs_C.adicionaAresta('1', 'A', 'B')
        self.nlw_bfs_C.adicionaAresta('11', 'F', 'B')
        self.nlw_bfs_C.adicionaAresta('12', 'G', 'B')
        self.nlw_bfs_C.adicionaAresta('17', 'B', 'E')
        self.nlw_bfs_C.adicionaAresta('3', 'A', 'J')
        self.nlw_bfs_C.adicionaAresta('10', 'H', 'F')
        self.nlw_bfs_C.adicionaAresta('4', 'K', 'G')
        self.nlw_bfs_C.adicionaAresta('8', 'I', 'G')

        # Eureliano

        self.euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.euleriano.adicionaAresta('a1', 'A', 'B')
        self.euleriano.adicionaAresta('a2', 'B', 'D')
        self.euleriano.adicionaAresta('a3', 'A', 'C')
        self.euleriano.adicionaAresta('a4', 'C', 'D')
        self.euleriano.adicionaAresta('a5', 'D', 'E')
        self.euleriano.adicionaAresta('a6', 'D', 'F')
        self.euleriano.adicionaAresta('a7', 'E', 'F')

        self.semi_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        
        self.semi_euleriano.adicionaAresta('a1', 'A', 'B')
        self.semi_euleriano.adicionaAresta('a2', 'A', 'C')
        self.semi_euleriano.adicionaAresta('a3', 'A', 'E')
        self.semi_euleriano.adicionaAresta('a4', 'B', 'E')
        self.semi_euleriano.adicionaAresta('a5', 'C', 'E')
        self.semi_euleriano.adicionaAresta('a6', 'D', 'E')
        self.semi_euleriano.adicionaAresta('a7', 'B', 'D')
        self.semi_euleriano.adicionaAresta('a8', 'C', 'D')
        self.semi_euleriano.adicionaAresta('a9', 'C', 'F')
        self.semi_euleriano.adicionaAresta('a10', 'D', 'F')

        self.v_v = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])

        self.v_v.adicionaAresta('a1', 'V1', 'V2')
        self.v_v.adicionaAresta('a2', 'V1', 'V3')
        self.v_v.adicionaAresta('a3', 'V3', 'V2')
        self.v_v.adicionaAresta('a4', 'V3', 'V4')
        self.v_v.adicionaAresta('a5', 'V4', 'V5')
        self.v_v.adicionaAresta('a6', 'V5', 'V8')
        self.v_v.adicionaAresta('a7', 'V5', 'V7')
        self.v_v.adicionaAresta('a8', 'V6', 'V7')

        # Não Eureliano

        self.nao_euleriano = MeuGrafo(['A', 'B', 'C', 'D', 'E'])

        self.nao_euleriano.adicionaAresta('a1', 'A', 'B')
        self.nao_euleriano.adicionaAresta('a2', 'A', 'C')
        self.nao_euleriano.adicionaAresta('a3', 'A', 'E')
        self.nao_euleriano.adicionaAresta('a4', 'B', 'E')
        self.nao_euleriano.adicionaAresta('a5', 'C', 'E')
        self.nao_euleriano.adicionaAresta('a6', 'D', 'E')
        self.nao_euleriano.adicionaAresta('a7', 'B', 'D')
        self.nao_euleriano.adicionaAresta('a8', 'C', 'D')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.nlw.dfs("A"), self.nlw_dfs_A)
        self.assertEqual(self.nlw.dfs("F"), self.nlw_dfs_F)
        self.assertEqual(self.nlw.dfs("K"), self.nlw_dfs_K)
        self.assertEqual(self.nlw.dfs("C"), self.nlw_dfs_C)
        self.assertEqual(self.g_p.dfs("J"), self.g_p_dfs_J)
        self.assertEqual(self.g_p.dfs("C"), self.g_p_dfs_C)
        self.assertEqual(self.g_p.dfs("Z"), self.g_p_dfs_Z)
        self.assertEqual(self.g_p.dfs("T"), self.g_p_dfs_T)


    def test_bfs(self):
        self.assertEqual(self.nlw.bfs("A"), self.nlw_bfs_A)
        self.assertEqual(self.nlw.bfs("K"), self.nlw_bfs_K)
        self.assertEqual(self.nlw.bfs("F"), self.nlw_bfs_F)
        self.assertEqual(self.nlw.bfs("C"), self.nlw_bfs_C)
        self.assertEqual(self.g_p.bfs("J"), self.g_p_bfs_J)
        self.assertEqual(self.g_p.bfs("T"), self.g_p_bfs_T)
        self.assertEqual(self.g_p.bfs("Z"), self.g_p_bfs_Z)
        self.assertEqual(self.g_p.bfs("P"), self.g_p_bfs_P)  

    def test_ha_ciclo(self):
        self.assertEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A'])
        self.assertEqual(self.g_l2.ha_ciclo(), ['A', 'a1', 'B', 'a3', 'A'])
        self.assertEqual(self.g_l3.ha_ciclo(), ['C', 'a2', 'C'])
        self.assertEqual(self.g_l4.ha_ciclo(), ['D', 'a1', 'D'])
        self.assertEqual(self.g_l5.ha_ciclo(), ['C', 'a2', 'C'])
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C'])
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a2', 'E', 'a4', 'C', 'a1', 'J'])
        self.assertEqual(self.g_c2.ha_ciclo(), False)
        self.assertEqual(self.g_c3.ha_ciclo(), False)
        self.assertEqual(self.g_p_dfs_J.ha_ciclo(), False)
        self.assertEqual(self.g_p_dfs_C.ha_ciclo(), False)
        self.assertEqual(self.g_p_dfs_Z.ha_ciclo(), False)
        self.assertEqual(self.g_p_dfs_T.ha_ciclo(), False)
   
    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertTrue(self.g_c3.conexo())
        self.assertTrue(self.nlw.conexo())
        self.assertTrue(self.nlw_dfs_A.conexo())
        self.assertTrue(self.nlw_dfs_K.conexo())
        self.assertTrue(self.nlw_dfs_F.conexo())
        self.assertTrue(self.nlw_dfs_C.conexo())
        self.assertTrue(self.nlw_bfs_A.conexo())
        self.assertTrue(self.nlw_bfs_K.conexo())
        self.assertTrue(self.nlw_bfs_F.conexo())
        self.assertTrue(self.nlw_bfs_C.conexo())
        self.assertTrue(self.nlw_bfs_C.conexo())
        self.assertFalse(self.g_v1.conexo())
        self.assertFalse(self.g_d.conexo())

    def test_euleriano(self):
        self.assertEqual(self.euleriano.printEulerPathCircuit(), ['A', 'a1', 'B', 'a2', 'D', 'a5', 'E', 'a7', 'F', 'a6', 'D', 'a4', 'C', 'a3', 'A'])
        self.assertEqual(self.semi_euleriano.printEulerPathCircuit(), ['B', 'a1', 'A', 'a2', 'C', 'a5', 'E', 'a4', 'B', 'a7', 'D', 'a8', 'C', 'a9', 'F', 'a10', 'D', 'a6', 'E', 'a3', 'A'])
        self.assertFalse(self.v_v.printEulerPathCircuit(),)
        self.assertFalse(self.g_p_dfs_C.printEulerPathCircuit(),)
        self.assertFalse(self.nao_euleriano.printEulerPathCircuit())
        self.assertEqual(self.nlw.printEulerPathCircuit(), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '2', 'A', '3', 'J', '5', 'K', '4', 'G', '6', 'J', '7', 'I', '8', 'G', '12', 'B', '13', 'C', '14', 'D', '15', 'E', '17', 'B', '16', 'D'])
        self.assertFalse(self.g_p.printEulerPathCircuit(),)
        self.assertFalse(self.g_p_sem_paralelas.printEulerPathCircuit(),)
        self.assertFalse(self.g_c.printEulerPathCircuit(),)

    def test_warshall(self):
        self.assertTrue(self.grafo_5.warshall())
