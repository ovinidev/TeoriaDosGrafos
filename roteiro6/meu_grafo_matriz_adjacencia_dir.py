from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

  def geraMatriz(self):
    '''
    Provê uma matriz do grafo contendo 0 e 1 de acordo com a presença de arestas
    :return: Uma matriz do grafo
    '''

    matriz_vazia = []

    for lin in range(len(self.M)):
      linha = []
      for col in range(len(self.M)):
        if (len(self.M[lin][col]) != 0):
          linha.append(1)
        else:
          linha.append(0)
      matriz_vazia.append(linha)

    return matriz_vazia

  def warshall(self):
    '''
    O algorítmo irá determinar a matriz de alcançabilidade (Rij) de um grafo.
    :return: Uma matriz do grafo após o algorítmo de warshall.
    '''

    matriz = self.geraMatriz()

    for i in range(len(matriz)):
      for j in range(len(matriz)):
        if matriz[j][i] == 1:
          for k in range(len(matriz)):
            if matriz[j][k] >= matriz[i][k]:
              matriz[j][k] = matriz[j][k]
            elif matriz[i][k] > matriz[j][k]:
              matriz[j][k] = matriz[i][k]

    return matriz

