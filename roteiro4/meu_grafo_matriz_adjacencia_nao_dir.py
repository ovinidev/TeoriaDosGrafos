from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
      '''
      Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
      Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
      :return: Uma lista com os pares de vértices não adjacentes
      '''
      pass

    def ha_laco(self):
      '''
      Verifica se existe algum laço no grafo.
      :return: Um valor booleano que indica se existe algum laço.
      '''
      for i in range(len(self.M)):
        if len(self.M[i][i]) > 0:
          return True
      
      return False

    def grau(self, V=''):
      '''
      Provê o grau do vértice passado como parâmetro
      :param V: O rótulo do vértice a ser analisado
      :return: Um valor inteiro que indica o grau do vértice
      :raises: VerticeInvalidoException se o vértice não existe no grafo
      '''
      if V not in self.N:
        raise VerticeInvalidoException("O vértice não existe no grafo")

      indice_vertice = self.N.index(V)
      grau = 0

      for i in range(indice_vertice, len(self.M)):
        if indice_vertice == i:
          grau += len(self.M[indice_vertice][i])*2
        else:
          grau += len(self.M[indice_vertice][i])

      for i in range(indice_vertice):
        grau += len(self.M[i][indice_vertice])
      return grau

    def ha_paralelas(self):
      '''
      Verifica se há arestas paralelas no grafo
      :return: Um valor booleano que indica se existem arestas paralelas no grafo.
      '''
      for i in range(len(self.M)):
        for j in range(len(self.M)):
          if len(self.M[i][j]) >= 2:
            return True
          if len(self.M[i][i]) >= 2:
            return True
          if len(self.M[j][j]) >= 2:
            return True

      return False

    def arestas_sobre_vertice(self, V):
      '''
      Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
      :param V: O vértice a ser analisado
      :return: Uma lista os rótulos das arestas que incidem sobre o vértice
      :raises: VerticeInvalidoException se o vértice não existe no grafo
      '''
      if V not in self.N:
        raise VerticeInvalidoException("O vértice não existe no grafo")
      
      for i in range(len(self.M)):
        for j in range(len(self.M)):
          x = self.M[i][j]
          aresta = x
          if(len(aresta) >= 1):
            print(aresta)
          if(self.M[i][j] == V):
            print("ok")

    def eh_completo(self):
      '''
      Verifica se o grafo é completo.
      :return: Um valor booleano que indica se o grafo é completo
      '''
      if self.ha_laco():
        return False

      if self.ha_paralelas():
        return False

      quantidade_de_vertices = len(self.N)

      for v in self.N:
        grau = self.grau(v)

        if grau != quantidade_de_vertices-1:
          return False  
      return True