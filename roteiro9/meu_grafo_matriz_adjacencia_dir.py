from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from math import inf

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

  def removeVertice(self, v):
    if self.existeVertice(v):

      index = 0

      for i in range(len(self.N)):
        if self.N[i] == v:
          index = i
          break
        
      self.M.pop(index)

      for j in range(len(self.M)):
        self.M[j].pop(index)
      
      self.N.pop(index)

    else:
      raise VerticeInvalidoException('O vértice {} não existe no grafo.'.format(v))

  def kahn(self):

    grafo = deepcopy(self)
    listaNaoFontes = []
    listaFontes = []

    while len(grafo.N) > 0: 
      for linha in range(len(grafo.M)):
        for coluna in range(len(grafo.M)):
          if len(grafo.M[linha][coluna]) > 0:
            if grafo.N[coluna] not in listaNaoFontes:
              listaNaoFontes.append(grafo.N[coluna])

          if grafo.N[linha] not in listaNaoFontes:
            if grafo.N[linha] not in listaFontes:
              listaFontes.append(grafo.N[linha])

      listaNaoFontes = []

      for vertices in listaFontes:
        if vertices not in grafo.N:
          continue
        grafo.removeVertice(vertices)

    return listaFontes
