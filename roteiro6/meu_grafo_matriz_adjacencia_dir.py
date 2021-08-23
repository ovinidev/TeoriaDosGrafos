from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

  def warshall(self):
    E = deepcopy(self)

    for i in range(len(E.M)):
      for j in range(len(E.M)):
        if len(E.M[j][i]) == 1:
          for k in range(len(E.M)):
            jk = len(self.M[j][k])
            ik = len(self.M[i][k])
            if jk > ik:
              E.M[j][k] = str(jk)
            elif jk == ik:
              E.M[j][k] = str(jk)
            elif ik > jk:
              E.M[j][k] = str(ik)

    return E