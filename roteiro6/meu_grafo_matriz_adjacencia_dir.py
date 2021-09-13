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
    cargaDoDrone = {}
    pi = {}
    beta = {}
    verticesNaoVisitados = []
    grafo = self.N

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
    arestas = []
    
    while w != destino:
      arestas = self.vAdjacentes(w)
      for r in arestas:
        if r in verticesNaoVisitados:
          if beta[r] >= (beta[w] + 1):
            beta[r] = (beta[w] + 1)
            pi[r] = w
            if r in listaDeCargas:
              cargaDoDrone[r] = cargaMaxima
            else:
              cargaDoDrone[r] = cargaDoDrone[w] - 1

      for i in verticesNaoVisitados:
        if cargaDoDrone[i] == 0 and i != origem:
          beta[i] = inf

      menorDosBetas = inf

      for r in verticesNaoVisitados:
        if beta[r] < menorDosBetas:
          menorDosBetas = beta[r]
          r_menorDosBetas = r

      if menorDosBetas == inf:
        return False

      aux = r_menorDosBetas
      verticesNaoVisitados.remove(aux)
      w = aux

    menorCaminho = []

    menorCaminho.append(destino)

    while destino != origem:
      menorCaminho.append(pi[destino])
      destino = pi[destino]

    menorCaminho.reverse()
    return menorCaminho