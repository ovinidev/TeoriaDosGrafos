from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo
dijkstraDoRoteiro = MeuGrafo(['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
'V11','V12','V13'])
dijkstraDoRoteiro.adicionaAresta('a1', 'V1', 'V4')
dijkstraDoRoteiro.adicionaAresta('a2', 'V2', 'V5')
dijkstraDoRoteiro.adicionaAresta('a3', 'V1', 'V3')
dijkstraDoRoteiro.adicionaAresta('a4', 'V1', 'V2')
dijkstraDoRoteiro.adicionaAresta('a5', 'V3', 'V6')
dijkstraDoRoteiro.adicionaAresta('a6', 'V4', 'V12')
dijkstraDoRoteiro.adicionaAresta('a7', 'V5', 'V9')
dijkstraDoRoteiro.adicionaAresta('a8', 'V4', 'V8')
dijkstraDoRoteiro.adicionaAresta('a9', 'V2', 'V3')
dijkstraDoRoteiro.adicionaAresta('a10', 'V5', 'V6')
dijkstraDoRoteiro.adicionaAresta('a11', 'V6', 'V10')
dijkstraDoRoteiro.adicionaAresta('a12', 'V6', 'V11')
dijkstraDoRoteiro.adicionaAresta('a13', 'V6', 'V7')


print(dijkstraDoRoteiro.drone('V1', 'V9', 3, 3, ['V5']))