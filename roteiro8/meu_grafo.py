from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from math import inf

class MeuGrafo(GrafoListaAdjacencia):

	def vertices_nao_adjacentes(self):
		'''
		Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
		Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
		:return: Uma lista com os pares de vértices não adjacentes
		'''

		vertices_nao_adjacentes = []

		for i in self.N:
				vertices_adjacentes = []

				for j in self.A:
						v1 = self.A[j].getV1()
						v2 = self.A[j].getV2()
						if v1 == i:
								vertices_adjacentes.append(v2)
						elif v2 == i:
								vertices_adjacentes.append(v1)

				for k in self.N:
						if k != i and k not in vertices_adjacentes:
								aresta1 = f'{i}-{k}'
								aresta2 = f'{k}-{i}'
								if aresta1 not in vertices_nao_adjacentes and aresta2 not in vertices_nao_adjacentes:
										vertices_nao_adjacentes.append(f'{i}-{k}')

				vertices_adjacentes = []

		return vertices_nao_adjacentes

	def ha_laco(self):
		'''
		Verifica se existe algum laço no grafo.
		:return: Um valor booleano que indica se existe algum laço.
		'''
		for a in self.A:
			if self.A[a].getV1() == self.A[a].getV2():
				return True
		return False

	def grau(self, V=''):
			'''
			Provê o grau do vértice passado como parâmetro
			:param V: O rótulo do vértice a ser analisado
			:return: Um valor inteiro que indica o grau do vértice
			:raises: VerticeInvalidoException se o vértice não existe no grafo
			'''

			cont_grau = 0
			temVertice = False

			for v in self.N:
					if v == V:
							temVertice = True

							for a in self.A:
									v1 = self.A[a].getV1()
									v2 = self.A[a].getV2()
									if v1 == v:
											cont_grau += 1
									if v2 == v:
											cont_grau += 1

			if temVertice == False and cont_grau == 0:
					raise VerticeInvalidoException(
							"O vértice", V, "não existe no grafo")
			else:
					return cont_grau

	def ha_paralelas(self):
			'''
			Verifica se há arestas paralelas no grafo
			:return: Um valor booleano que indica se existem arestas paralelas no grafo.
			'''
			existeArestasParalelas = False
			for v in self.N:
					vertices_adjacentes = []

					for a in self.A:
							v1 = self.A[a].getV1()
							v2 = self.A[a].getV2()
							if v1 == v:
									vertices_adjacentes.append(v2)
							if v2 == v:
									vertices_adjacentes.append(v1)
					for vertices in (vertices_adjacentes):
							qtd_repeticoes = vertices_adjacentes.count(vertices)
							if qtd_repeticoes >= 2:
									return True

			return False

	def arestas_sobre_vertice(self, V):
			'''
			Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
			:param V: O vértice a ser analisado
			:return: Uma lista os rótulos das arestas que incidem sobre o vértice
			:raises: VerticeInvalidoException se o vértice não existe no grafo
			'''
			tem_vertice = False
			vertices_adjacentes = []

			for v in self.N:

					if v == V:
							tem_vertice = True

			for a in self.A:
					v1 = self.A[a].getV1()
					v2 = self.A[a].getV2()
					if v1 == V or v2 == V:
							vertices_adjacentes.append(a)

			if(tem_vertice == False):
					raise VerticeInvalidoException(
							"O vértice", V, "não existe no grafo")
			else:
					return vertices_adjacentes

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

	def verticesAdjacentes(self):
			'''
			Função para gerar uma lista dos vertices adjacentes
			:return: Uma lista com os vértices adjacentes
			'''

			vertices_adjacentes = []

			for a in self.A:
					arestaAtual = self.A[a]
					verticeAtual1 = arestaAtual.getV1()
					verticeAtual2 = arestaAtual.getV2()

					if verticeAtual1 not in vertices_adjacentes:
							vertices_adjacentes.append((verticeAtual1, a, verticeAtual2))

			return vertices_adjacentes

	def arestaMenorPeso(self):
		listaArestas = list(self.A)
		menorPeso = listaArestas[0]

		for a in self.A:
			if (self.A[a].getPeso() < self.A[menorPeso].getPeso()):
				menorPeso = a

		return self.A[menorPeso].getV1()


	def prim(self):

		verticeInicial = self.arestaMenorPeso()

		novoGrafo = MeuGrafo([verticeInicial])
		listaDeVertices = [verticeInicial]

		while len(listaDeVertices) != len(self.N):
			vMenorPeso = inf
			verticeForaDaArvore = 0 
			arestaMenorPeso = 0

			for a in self.A:
				arestaAtual = self.A[a]
				vertice1 = arestaAtual.getV1()
				vertice2 = arestaAtual.getV2()

				if vertice1 in listaDeVertices and vertice2 not in listaDeVertices:
					if arestaAtual.getPeso() < vMenorPeso:
						vMenorPeso = arestaAtual.getPeso()
						arestaMenorPeso = a
						verticeForaDaArvore = vertice2

				elif vertice2 in listaDeVertices and vertice1 not in listaDeVertices:
					if arestaAtual.getPeso() < vMenorPeso:
						vMenorPeso = arestaAtual.getPeso()
						arestaMenorPeso = a
						verticeForaDaArvore = vertice1

			arestaMenorPeso = self.A[arestaMenorPeso]
			listaDeVertices.append(verticeForaDaArvore)
			novoGrafo.adicionaVertice(verticeForaDaArvore)

			aresta = arestaMenorPeso.getRotulo()
			v1 = arestaMenorPeso.getV1()
			v2 = arestaMenorPeso.getV2()
			peso = arestaMenorPeso.getPeso()

			novoGrafo.adicionaAresta(aresta,v1, v2, peso)
			
		return novoGrafo
