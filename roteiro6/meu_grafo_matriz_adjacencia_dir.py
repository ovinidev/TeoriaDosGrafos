from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

  def warshall(self):
    copia_grafo = deepcopy(self)

    for i in range(len(self.M)):
      for j in range(len(self.M)):
        if len(self.M[i][j]) == 1:
          for k in range(len(self.M[i][j])):
            copia_grafo[j][k] += max(M[j][k], M[i][k])