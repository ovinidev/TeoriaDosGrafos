from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo
cursoEngComputacao = MeuGrafo(['7', '5', '3', '11', '8', '2', '9', '10'])

cursoEngComputacao.adicionaAresta("a1", "7", "8")
cursoEngComputacao.adicionaAresta("a2", "5", "8")
cursoEngComputacao.adicionaAresta("a3", "5", "10")
cursoEngComputacao.adicionaAresta("a4", "11", "10")
cursoEngComputacao.adicionaAresta("a5", "8", "9")
cursoEngComputacao.adicionaAresta("a6", "11", "9")
cursoEngComputacao.adicionaAresta("a7", "11", "2")
cursoEngComputacao.adicionaAresta("a8", "7", "11")
cursoEngComputacao.adicionaAresta("a9", "3", "11")


print(cursoEngComputacao.kahn())