from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

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
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
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
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
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

    def verticesAdjacentes_aux(self):

        vertices_adjacentes = []

        for a in self.A:
            arestaAtual = self.A[a]
            verticeAtual1 = arestaAtual.getV1()
            verticeAtual2 = arestaAtual.getV2()

            vertices_adjacentes.append(verticeAtual1)
            vertices_adjacentes.append(a)

        return vertices_adjacentes
        
    def dfs_Recursivo(self, V, dfs, verticePercorrido, v_Adjacentes):
        '''
        Função recursiva para percorrer o grafo
        :param V: O vértice raíz, o grafo dfs, os vertices percorridos e adjacentes
        '''

        verticePercorrido.append(V)

        verticesAdjacentes = []
        for v in v_Adjacentes:
            if v[0] == V:
                verticesAdjacentes.append(v)
            elif v[-1] == V:
                if len(v) > 5:
                    verticesAdjacentes.append((v[-1] + v[1] + v[0]))
                else:
                    verticesAdjacentes.append((v[-1], v[1], v[0]))

        for i in verticesAdjacentes:
            if len(i) > 5:
                if i[-1] not in verticePercorrido:
                    dfs.adicionaAresta((i[1],i[0],i[-1]))
                    self.dfs_Recursivo(i[-1],dfs,verticePercorrido,v_Adjacentes) 
            else:
                if i[-1] not in verticePercorrido:
                    dfs.adicionaAresta(i[1], i[0],i[-1])
                    self.dfs_Recursivo( i[-1],dfs,verticePercorrido,v_Adjacentes) 
                

    def dfs(self, V=''):
        '''
        Provê um novo grafo após realizar o dfs
        :param V: O vértice raíz
        :return: Uma lista com o novo grafo pós dfs
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        dfs = MeuGrafo(self.N[::])

        temVertice = False
        for v in self.N:
            if v == V:
                temVertice = True

        VerticesAdjacentes = self.verticesAdjacentes()
        VerticesPercorrido = []

        self.dfs_Recursivo(V, dfs, VerticesPercorrido, VerticesAdjacentes)

        if temVertice == False:
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
        else:
            return dfs
            
    def bfs(self, V=''):
        '''
        Provê um novo grafo após realizar o bfs
        :param V: O vértice raíz
        :return: Uma lista com o novo grafo pós bfs
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        bfs = MeuGrafo(self.N[::])

        verticesVisitados = [V]
        fila = [V]

        temVertice = False

        for v in self.N:
            if v == V:
                temVertice = True

        while(len(fila) != 0):
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1
                    
                    if verticeAdjacente not in verticesVisitados:
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)                        
                        bfs.adicionaAresta(a, verticeAnalisado, verticeAdjacente)
                
            fila.pop(0)

        if(temVertice == False):
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
        else: 
            return bfs


    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Um valor booleano que indica se o grafo é ou não conexo
        '''
        grafo_bfs = self.bfs_aux(self.N[0])
        tamanhoGrafoBfs = len(grafo_bfs)
        tamanhoGrafoAnalisado = len(self.N)

        if (tamanhoGrafoBfs != tamanhoGrafoAnalisado):
            return False
        else:
            return True

    def bfs_aux(self, V=''):
        bfs = MeuGrafo(self.N[::])

        verticesVisitados = [V]
        fila = [V]
        listaBfs = [V]

        while(len(fila) != 0):
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1
                    
                    if verticeAdjacente not in verticesVisitados:
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)                        
                        bfs.adicionaAresta(a, verticeAnalisado, verticeAdjacente)
                        listaBfs.append(verticeAdjacente)
                
            fila.pop(0)
        return listaBfs


    def dfs_Recursivo_aux(self, V, dfs, verticePercorrido, v_Adjacentes, lista_dfs, arestasPercorridas , ciclo):
        '''
        Função recursiva para percorrer o grafo
        :param V: O vértice raíz, o grafo dfs, os vertices percorridos e adjacentes
        '''
        
        verticePercorrido.append(V)
        verticesAdjacentes = []
        
        for v in v_Adjacentes:
            if v[0] == V:
                verticesAdjacentes.append(v)
            elif v[-1] == V:
                if len(v) > 5:
                    verticesAdjacentes.append((v[-1] + v[1] + v[0]))
                else:
                    verticesAdjacentes.append((v[-1], v[1], v[0]))

        for i in verticesAdjacentes:
            if i[-1] == verticePercorrido[0] and i[1] not in arestasPercorridas:
                ciclo.append(i[-1])
                break
            
            if (len(ciclo) > 0):
                break

            if i[-1] not in verticePercorrido:
                arestasPercorridas.append(i[1])
                lista_dfs.append(i[1])
                lista_dfs.append(i[-1])
                self.dfs_Recursivo_aux(i[-1], dfs, verticePercorrido, v_Adjacentes, lista_dfs, arestasPercorridas, ciclo)
        if (len(ciclo) > 0):
            for a in self.A:
                if (self.A[a].getV1() == V and self.A[a].getV2() == ciclo[-1]):
                    if (a not in ciclo):
                        ciclo.append(a)
                        break

                if (self.A[a].getV2() == V and self.A[a].getV1() == ciclo[-1]):
                    if (a not in ciclo):
                        ciclo.append(a)
                        break
                    
            ciclo.append(V)
                
    def dfs_aux(self, V=''):
        '''
        Provê um novo grafo após realizar o dfs
        :param V: O vértice raíz
        :return: Uma lista com o novo grafo pós dfs
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        dfs = MeuGrafo(self.N[::])
        lista_dfs = [V]
        temVertice = False
        for v in self.N:
            if v == V:
                temVertice = True

        VerticesAdjacentes = self.verticesAdjacentes()
        VerticesPercorrido = []
        arestasPercorridas = []
        ciclo = []

        self.dfs_Recursivo_aux(V, dfs, VerticesPercorrido, VerticesAdjacentes, lista_dfs, arestasPercorridas, ciclo)

        if temVertice == False:
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
        else:
            return ciclo
            
    def ha_ciclo(self):
        '''
        Verifica se o grafo há ciclo
        :return: Um valor booleano que indica se existe ou não um ciclo
        '''

        for i in (self.N):
            grafo_dfs = self.dfs_aux(i)

            if len(grafo_dfs) > 0:
                return grafo_dfs

        return False

    def ha_euleriano(self):
        '''
        Verifica se o grafo é euleriano
        :return: Um valor booleano que indica se é possível realizar o algorítmo euleriano
        '''

        if (not self.conexo()):
            return False
        
        qtd_impares = 0

        for v in self.N:
            grau = self.grau(v)
            if (grau % 2 == 1):
                qtd_impares += 1
    
        if (qtd_impares == 0 or qtd_impares == 2):
            return True
        
        return False

    def eh_ponte(self, A=''):
        '''
        Verifica se no vértice passado há ponte
        :return: Um valor booleano que indica se o vértice é ponte
        '''

        copia_grafo = deepcopy(self)

        copia_grafo.removeAresta(A)

        for v in copia_grafo.N:
            if (copia_grafo.grau(v) == 0):
                copia_grafo.removeVertice(v)

        if (copia_grafo.conexo()): return False

        else: return True
        
    def printEulerPathCircuit(self):
        
        if (not self.ha_euleriano()): return False

        copia_grafo = deepcopy(self)

        qtd_impares = 0
        vertice_grau_impar = 0

        for v in self.N:
            grau = self.grau(v)
            if (grau % 2 == 1):
                qtd_impares += 1
                vertice_grau_impar = v

        if (qtd_impares == 0):
            self.printEuler("A")
        elif (qtd_impares == 2):
            self.printEuler(vertice_grau_impar)
        else:
            print("Nao existe euler")


    def printEuler(self, V=''):

        copia_grafo = deepcopy(self)

        vertice_adjacente = copia_grafo.verticesAdjacentes_(V)

        aresta_adjacente = copia_grafo.arestas_sobre_vertice(V)


        if (not vertice_adjacente):
            return

        if (len(vertice_adjacente) == 1):
            vertice = vertice_adjacente[0]
            vertice_adjacente.remove(vertice)
            return

        for a in aresta_adjacente:
            if (not self.eh_ponte(a)):
                vertice = vertice_adjacente[0]
                copia_grafo.removeAresta(a)
                self.printEuler(vertice)
                return


    def verticesAdjacentes_(self, V=''):

        vertices_adjacentes = []

        for a in self.A:
            arestaAtual = self.A[a]
            verticeAtual1 = arestaAtual.getV1()
            verticeAtual2 = arestaAtual.getV2()

            if (verticeAtual1 == V or verticeAtual2 == V):
                vertices_adjacentes.append(verticeAtual1)
                vertices_adjacentes.append(verticeAtual2)
                vertices_adjacentes.remove(V)

        return vertices_adjacentes
