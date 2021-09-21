from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from math import inf

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

  def vAdjacentes(self, v):
    adjacentes = []

    for i in range(len(self.M)):
      for k in range(len(self.M)):
        if (len(self.M[i][k]) > 0):
          if (self.N[i] == v):
            adjacentes.append(self.N[k])
    return adjacentes

  def drone(self, origem, destino, cargaInicial, cargaMaxima, listaDeCargas = []):
    '''
    Provê uma lista aplicando o algotimo de dijkstra modificado
    :param V: o vertice origem, vertice destino, carga inicial, carga máxima, 
    lista de vertices com pontos de carga.
    :return: lista com o menor caminho do grafo
    :raises: VerticeInvalidoException se o vértice não existe no grafo
    '''
    grafo = self.N
    cargaDoDrone = {}
    pi = {}
    beta = {}
    verticesNaoVisitados = []

    if (origem not in grafo or destino not in grafo):
      raise VerticeInvalidoException("O vértice não existe no grafo")

    # Adicionando os valores iniciais
    for v in grafo:
      beta[v] = inf
      cargaDoDrone[v] = inf
      verticesNaoVisitados.append(v)
    beta[origem] = 0

    if origem in listaDeCargas:
      cargaDoDrone[origem] = cargaMaxima
    else:
      cargaDoDrone[origem] = cargaInicial

    verticesNaoVisitados.remove(origem)
    w = origem
    aux = 0
    a = []
    
    while w != destino:
      a = self.vAdjacentes(w)
      for r in a:
        if (r in verticesNaoVisitados):
          if (beta[r] >= (beta[w] + 1)):
            beta[r] = (beta[w] + 1)
            pi[r] = w
            if r in listaDeCargas:
              cargaDoDrone[r] = cargaMaxima
            else:
              cargaDoDrone[r] = cargaDoDrone[w] - 1

      for i in verticesNaoVisitados:
        if (cargaDoDrone[i] == 0 and i != origem):
          beta[i] = inf

      menorDosBetas = inf

      for i in verticesNaoVisitados:
        if (beta[i] < menorDosBetas):
          menorDosBetas = beta[i]
          betaMenor = i

      if (menorDosBetas == inf):
        return False

      aux = betaMenor
      verticesNaoVisitados.remove(aux)
      w = aux

    menorCaminhoDrone = []

    menorCaminhoDrone.append(destino)

    while destino != origem:
      menorCaminhoDrone.append(pi[destino])
      destino = pi[destino]

    menorCaminhoDrone.reverse()
    return menorCaminhoDrone

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
