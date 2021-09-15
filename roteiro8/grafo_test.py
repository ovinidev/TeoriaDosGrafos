import unittest
from bibgrafo.grafo_exceptions import *
from meu_grafo import *

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

        #Arvore Prim

        self.nlw_prim = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])
        self.nlw_prim.adicionaAresta('1', 'A', 'B')
        self.nlw_prim.adicionaAresta('2', 'A', 'G')
        self.nlw_prim.adicionaAresta('3', 'A', 'J')
        self.nlw_prim.adicionaAresta('4', 'K', 'G')
        self.nlw_prim.adicionaAresta('7', 'J', 'I')
        self.nlw_prim.adicionaAresta('9', 'G', 'H')
        self.nlw_prim.adicionaAresta('10', 'H', 'F')
        self.nlw_prim.adicionaAresta('13', 'B', 'C')
        self.nlw_prim.adicionaAresta('14', 'C', 'D')
        self.nlw_prim.adicionaAresta('15', 'D', 'E')

        self.grafo_roteiro_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafo_roteiro_prim.adicionaAresta('a1', 'A', 'B', 1)
        self.grafo_roteiro_prim.adicionaAresta('a2', 'B', 'C', 2)
        self.grafo_roteiro_prim.adicionaAresta('a3', 'C', 'G', 2)
        self.grafo_roteiro_prim.adicionaAresta('a6', 'E', 'G', 1)
        self.grafo_roteiro_prim.adicionaAresta('a7', 'E', 'D', 2)
        self.grafo_roteiro_prim.adicionaAresta('a4', 'G', 'F', 3)


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

    def test_prim(self):
        self.assertEqual(self.nlw.prim(), self.nlw_prim)
        self.assertEqual(self.grafo_roteiro.prim(), self.grafo_roteiro_prim)