from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo
cursoEngComputacao = MeuGrafo([
            "11", "12", "13", "14", "15","16", "17",
            "21", "22", "23","24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36",
            "41", "42", "43", "44", "45",
            "51", "52", "53", "54", "55",
            "61", "62", "63", "64", "65",
            "71", "72", "73", "74", "75",
            "81", "82", "83", "84", "85",
            "91", "92", "93", "94",
            "101", "102", "103"])

cursoEngComputacao.adicionaAresta("d1", "11", "21")
cursoEngComputacao.adicionaAresta("d2", "14", "24")
cursoEngComputacao.adicionaAresta("d3", "14", "25")
cursoEngComputacao.adicionaAresta("d4", "14", "34")
cursoEngComputacao.adicionaAresta("d5", "14", "35")
cursoEngComputacao.adicionaAresta("d6", "15", "24")
cursoEngComputacao.adicionaAresta("d7", "15", "25")
cursoEngComputacao.adicionaAresta("d8", "15", "34")
cursoEngComputacao.adicionaAresta("d9", "15", "35")
cursoEngComputacao.adicionaAresta("d10", "16", "26")
cursoEngComputacao.adicionaAresta("d11", "21", "31")
cursoEngComputacao.adicionaAresta("d12", "21", "41")
cursoEngComputacao.adicionaAresta("d13", "24", "33")
cursoEngComputacao.adicionaAresta("d14", "24", "43")
cursoEngComputacao.adicionaAresta("d15", "24", "44")
cursoEngComputacao.adicionaAresta("d16", "24", "53")
cursoEngComputacao.adicionaAresta("d17", "24", "54")
cursoEngComputacao.adicionaAresta("d18", "24", "72")
cursoEngComputacao.adicionaAresta("d19", "26", "36")
cursoEngComputacao.adicionaAresta("d20", "31", "51")
cursoEngComputacao.adicionaAresta("d21", "31", "52")
cursoEngComputacao.adicionaAresta("d22", "31", "64")
cursoEngComputacao.adicionaAresta("d23", "34", "63")
cursoEngComputacao.adicionaAresta("d24", "35", "63")
cursoEngComputacao.adicionaAresta("d25", "34", "81")
cursoEngComputacao.adicionaAresta("d26", "35", "81")
cursoEngComputacao.adicionaAresta("d27", "36", "44")
cursoEngComputacao.adicionaAresta("d28", "36", "45")
cursoEngComputacao.adicionaAresta("d29", "36", "55")
cursoEngComputacao.adicionaAresta("d30", "43", "62")
cursoEngComputacao.adicionaAresta("d31", "44", "55")
cursoEngComputacao.adicionaAresta("d32", "44", "93")
cursoEngComputacao.adicionaAresta("d33", "45", "93")
cursoEngComputacao.adicionaAresta("d34", "51", "61")
cursoEngComputacao.adicionaAresta("d35", "52", "75")
cursoEngComputacao.adicionaAresta("d36", "54", "81")
cursoEngComputacao.adicionaAresta("d37", "55", "65")
cursoEngComputacao.adicionaAresta("d38", "61", "84")
cursoEngComputacao.adicionaAresta("d39", "61", "94")
cursoEngComputacao.adicionaAresta("d40", "63", "73")
cursoEngComputacao.adicionaAresta("d41", "64", "75")
cursoEngComputacao.adicionaAresta("d42", "64", "84")
cursoEngComputacao.adicionaAresta("d43", "73", "82")
cursoEngComputacao.adicionaAresta("d44", "74", "83")
cursoEngComputacao.adicionaAresta("d45", "75", "85")
cursoEngComputacao.adicionaAresta("d46", "75", "94")
cursoEngComputacao.adicionaAresta("d47", "83", "92")
cursoEngComputacao.adicionaAresta("d48", "92", "103")


print(cursoEngComputacao.topologico())