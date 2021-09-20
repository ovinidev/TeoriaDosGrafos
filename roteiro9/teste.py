from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado

from meu_grafo_matriz_adjacencia_dir import MeuGrafo
cursoConstrEdificios = MeuGrafo([
  '11', '12', '13', '14', '15', '16', '17', '18',
  '21', '22', '23', '24', '25', '26', '27',
  '31', '32', '33', '34', '35', '36', '37', '38',
  '41', '42', '43', '44', '45', '46', '47',
  '51', '52', '53', '54', '55', '56', '57', '58',
  '61', '62', '63', '64', '65', '66', '67', '68',
  '71', '72', '73'])

cursoConstrEdificios.adicionaAresta('d1', '21', '15')
cursoConstrEdificios.adicionaAresta('d2', '23', '14')
cursoConstrEdificios.adicionaAresta('d3', '24', '11')
cursoConstrEdificios.adicionaAresta('d4', '24', '17')
cursoConstrEdificios.adicionaAresta('d5', '25', '15')
cursoConstrEdificios.adicionaAresta('d6', '26', '17')
cursoConstrEdificios.adicionaAresta('d7', '27', '17')
cursoConstrEdificios.adicionaAresta('d8', '32', '15')
cursoConstrEdificios.adicionaAresta('d9', '32', '21')
cursoConstrEdificios.adicionaAresta('d10', '33', '21')
cursoConstrEdificios.adicionaAresta('d11', '33', '25')
cursoConstrEdificios.adicionaAresta('d12', '34', '15')
cursoConstrEdificios.adicionaAresta('d13', '35', '11')
cursoConstrEdificios.adicionaAresta('d14', '35', '27')
cursoConstrEdificios.adicionaAresta('d15', '35', '35')
cursoConstrEdificios.adicionaAresta('d16', '36', '26')
cursoConstrEdificios.adicionaAresta('d17', '37', '23')
cursoConstrEdificios.adicionaAresta('18', '38', '24')
cursoConstrEdificios.adicionaAresta('19', '41', '17')
cursoConstrEdificios.adicionaAresta('20', '41', '21')
cursoConstrEdificios.adicionaAresta('21', '42', '17')
cursoConstrEdificios.adicionaAresta('22', '42', '21')
cursoConstrEdificios.adicionaAresta('23', '43', '23')
cursoConstrEdificios.adicionaAresta('24', '44', '24')
cursoConstrEdificios.adicionaAresta('25', '45', '36')
cursoConstrEdificios.adicionaAresta('26', '45', '37')
cursoConstrEdificios.adicionaAresta('27', '46', '17')
cursoConstrEdificios.adicionaAresta('28', '46', '32')
cursoConstrEdificios.adicionaAresta('29', '47', '11')
cursoConstrEdificios.adicionaAresta('30', '47', '37')
cursoConstrEdificios.adicionaAresta('31', '51', '37')
cursoConstrEdificios.adicionaAresta('32', '51', '43')
cursoConstrEdificios.adicionaAresta('33', '51', '45')
cursoConstrEdificios.adicionaAresta('34', '51', '46')
cursoConstrEdificios.adicionaAresta('35', '52', '41')
cursoConstrEdificios.adicionaAresta('36', '52', '42')
cursoConstrEdificios.adicionaAresta('37', '52', '45')
cursoConstrEdificios.adicionaAresta('38', '52', '46')
cursoConstrEdificios.adicionaAresta('39', '53', '17')
cursoConstrEdificios.adicionaAresta('40', '53', '32')
cursoConstrEdificios.adicionaAresta('41', '54', '47')
cursoConstrEdificios.adicionaAresta('42', '55', '17')
cursoConstrEdificios.adicionaAresta('43', '55', '32')
cursoConstrEdificios.adicionaAresta('44', '56', '46')
cursoConstrEdificios.adicionaAresta('45', '57', '43')
cursoConstrEdificios.adicionaAresta('46', '62', '31')
cursoConstrEdificios.adicionaAresta('47', '62', '44')
cursoConstrEdificios.adicionaAresta('48', '64', '22')
cursoConstrEdificios.adicionaAresta('49', '64', '27')
cursoConstrEdificios.adicionaAresta('50', '64', '33')
cursoConstrEdificios.adicionaAresta('51', '64', '36')
cursoConstrEdificios.adicionaAresta('52', '65', '47')
cursoConstrEdificios.adicionaAresta('53', '66', '22')
cursoConstrEdificios.adicionaAresta('54', '67', '31')

print(cursoConstrEdificios)