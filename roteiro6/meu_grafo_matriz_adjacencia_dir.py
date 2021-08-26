from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

  def warshall(self):

    matriz = []

    for l in range(len(self.M)):
      linha = []
      for c in range(len(self.M)):
        if (len(self.M[l][c]) > 0):
          linha.append(1)
        else:
          linha.append(0)
      matriz.append(linha)

    for i in range(len(matriz)):
      for j in range(len(matriz)):
        if matriz[j][i] == 1:
          for k in range(len(matriz)):
            jk = matriz[j][k]
            ik = matriz[i][k]
            if jk >= ik:
              matriz[j][k] = jk
            elif ik > jk:
              matriz[j][k] = ik

    return matriz