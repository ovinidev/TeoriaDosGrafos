import unittest
from bibgrafo.grafo_exceptions import *
from meu_grafo_matriz_adjacencia_dir import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        self.cursoMatematica = MeuGrafo([
            "11", "12", "13", "14", "15","16", "17",
            "21", "22", "23","24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36",
            "41", "42", "43", "44", "45", "46",
            "51", "52", "53", "54", "55", "56","57",
            "61", "62", "63", "64", "65", "66","67",
            "71", "72", "73", "74", "75", "77",
            "81", "82", "83", "84", "85", "87"])

        self.cursoMatematica.adicionaAresta("d1", "11", "21")
        self.cursoMatematica.adicionaAresta("d2", "11", "22")
        self.cursoMatematica.adicionaAresta("d3", "13", "22")
        self.cursoMatematica.adicionaAresta("d4", "16", "26")
        self.cursoMatematica.adicionaAresta("d5", "21", "31")
        self.cursoMatematica.adicionaAresta("d6", "22", "32")
        self.cursoMatematica.adicionaAresta("d7", "12", "33")
        self.cursoMatematica.adicionaAresta("d8", "12", "34")
        self.cursoMatematica.adicionaAresta("d9", "21", "41")
        self.cursoMatematica.adicionaAresta("d10", "23", "41")
        self.cursoMatematica.adicionaAresta("d11", "23", "42")
        self.cursoMatematica.adicionaAresta("d12", "32", "42")
        self.cursoMatematica.adicionaAresta("d13", "36", "43")
        self.cursoMatematica.adicionaAresta("d14", "34", "44")
        self.cursoMatematica.adicionaAresta("d15", "27", "45")
        self.cursoMatematica.adicionaAresta("d16", "33", "51")
        self.cursoMatematica.adicionaAresta("d17", "12", "52")
        self.cursoMatematica.adicionaAresta("d18", "32", "53")
        self.cursoMatematica.adicionaAresta("d19", "44", "54")
        self.cursoMatematica.adicionaAresta("d20", "44", "55")
        self.cursoMatematica.adicionaAresta("d21", "44", "57")
        self.cursoMatematica.adicionaAresta("d22", "51", "61")
        self.cursoMatematica.adicionaAresta("d23", "52", "62")
        self.cursoMatematica.adicionaAresta("d24", "32", "63")
        self.cursoMatematica.adicionaAresta("d25", "54", "64")
        self.cursoMatematica.adicionaAresta("d26", "46", "65")
        self.cursoMatematica.adicionaAresta("d27", "57", "67")
        self.cursoMatematica.adicionaAresta("d28", "42", "71")
        self.cursoMatematica.adicionaAresta("d29", "22", "72")
        self.cursoMatematica.adicionaAresta("d30", "41", "73")
        self.cursoMatematica.adicionaAresta("d31", "42", "73")
        self.cursoMatematica.adicionaAresta("d32", "64", "74")
        self.cursoMatematica.adicionaAresta("d33", "65", "75")
        self.cursoMatematica.adicionaAresta("d34", "67", "77")
        self.cursoMatematica.adicionaAresta("d35", "62", "81")
        self.cursoMatematica.adicionaAresta("d36", "75", "82")
        self.cursoMatematica.adicionaAresta("d37", "32", "83")
        self.cursoMatematica.adicionaAresta("d38", "74", "84")
        self.cursoMatematica.adicionaAresta("d39", "77", "87")

        self.cursoConstrEdificios = MeuGrafo([
        '11', '12', '13', '14', '15', '16', '17', '18',
        '21', '22', '23', '24', '25', '26', '27',
        '31', '32', '33', '34', '35', '36', '37', '38',
        '41', '42', '43', '44', '45', '46', '47',
        '51', '52', '53', '54', '55', '56', '57', '58',
        '61', '62', '63', '64', '65', '66', '67', '68',
        '71', '72', '73'])

        self.cursoConstrEdificios.adicionaAresta('d1', '15', '21')
        self.cursoConstrEdificios.adicionaAresta('d2', '14', '23')
        self.cursoConstrEdificios.adicionaAresta('d3', '11', '24')
        self.cursoConstrEdificios.adicionaAresta('d4', '17', '24')
        self.cursoConstrEdificios.adicionaAresta('d5', '15', '25')
        self.cursoConstrEdificios.adicionaAresta('d6', '17', '26')
        self.cursoConstrEdificios.adicionaAresta('d7', '17', '27')
        self.cursoConstrEdificios.adicionaAresta('d8', '15', '32')
        self.cursoConstrEdificios.adicionaAresta('d9', '21', '32')
        self.cursoConstrEdificios.adicionaAresta('d10', '21', '33')
        self.cursoConstrEdificios.adicionaAresta('d11', '25', '33')
        self.cursoConstrEdificios.adicionaAresta('d12', '15', '34')
        self.cursoConstrEdificios.adicionaAresta('d13', '11', '35')
        self.cursoConstrEdificios.adicionaAresta('d14', '27', '35')
        self.cursoConstrEdificios.adicionaAresta('15', '26', '36')
        self.cursoConstrEdificios.adicionaAresta('16', '23', '37')
        self.cursoConstrEdificios.adicionaAresta('17', '24', '38')
        self.cursoConstrEdificios.adicionaAresta('18', '17', '41')
        self.cursoConstrEdificios.adicionaAresta('19', '21', '41')
        self.cursoConstrEdificios.adicionaAresta('20', '17', '42')
        self.cursoConstrEdificios.adicionaAresta('21', '21', '42')
        self.cursoConstrEdificios.adicionaAresta('22', '23', '43')
        self.cursoConstrEdificios.adicionaAresta('23', '24', '44')
        self.cursoConstrEdificios.adicionaAresta('24', '36', '45')
        self.cursoConstrEdificios.adicionaAresta('25', '37', '45')
        self.cursoConstrEdificios.adicionaAresta('26', '17', '46')
        self.cursoConstrEdificios.adicionaAresta('27', '32', '46')
        self.cursoConstrEdificios.adicionaAresta('28', '11', '47')
        self.cursoConstrEdificios.adicionaAresta('29', '37', '47')
        self.cursoConstrEdificios.adicionaAresta('30', '37', '51')
        self.cursoConstrEdificios.adicionaAresta('31', '43', '51')
        self.cursoConstrEdificios.adicionaAresta('32', '45', '51')
        self.cursoConstrEdificios.adicionaAresta('33', '46', '51')
        self.cursoConstrEdificios.adicionaAresta('34', '41', '52')
        self.cursoConstrEdificios.adicionaAresta('35', '42', '52')
        self.cursoConstrEdificios.adicionaAresta('36', '45', '52')
        self.cursoConstrEdificios.adicionaAresta('37', '46', '52')
        self.cursoConstrEdificios.adicionaAresta('38', '17', '53')
        self.cursoConstrEdificios.adicionaAresta('39', '32', '53')
        self.cursoConstrEdificios.adicionaAresta('40', '47', '54')
        self.cursoConstrEdificios.adicionaAresta('41', '17', '55')
        self.cursoConstrEdificios.adicionaAresta('42', '32', '55')
        self.cursoConstrEdificios.adicionaAresta('43', '46', '56')
        self.cursoConstrEdificios.adicionaAresta('44', '43', '57')
        self.cursoConstrEdificios.adicionaAresta('45', '31', '62')
        self.cursoConstrEdificios.adicionaAresta('46', '44', '62')
        self.cursoConstrEdificios.adicionaAresta('47', '22', '64')
        self.cursoConstrEdificios.adicionaAresta('48', '27', '64')
        self.cursoConstrEdificios.adicionaAresta('49', '33', '64')
        self.cursoConstrEdificios.adicionaAresta('50', '36', '64')
        self.cursoConstrEdificios.adicionaAresta('51', '47', '65')
        self.cursoConstrEdificios.adicionaAresta('52', '22', '66')
        self.cursoConstrEdificios.adicionaAresta('53', '31', '67')

        self.cursoEngComputacao = MeuGrafo([
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

        self.cursoEngComputacao.adicionaAresta("d1", "11", "21")
        self.cursoEngComputacao.adicionaAresta("d2", "14", "24")
        self.cursoEngComputacao.adicionaAresta("d3", "14", "25")
        self.cursoEngComputacao.adicionaAresta("d4", "14", "34")
        self.cursoEngComputacao.adicionaAresta("d5", "14", "35")
        self.cursoEngComputacao.adicionaAresta("d6", "15", "24")
        self.cursoEngComputacao.adicionaAresta("d7", "15", "25")
        self.cursoEngComputacao.adicionaAresta("d8", "15", "34")
        self.cursoEngComputacao.adicionaAresta("d9", "15", "35")
        self.cursoEngComputacao.adicionaAresta("d10", "16", "26")
        self.cursoEngComputacao.adicionaAresta("d11", "21", "31")
        self.cursoEngComputacao.adicionaAresta("d12", "21", "41")
        self.cursoEngComputacao.adicionaAresta("d13", "24", "33")
        self.cursoEngComputacao.adicionaAresta("d14", "24", "43")
        self.cursoEngComputacao.adicionaAresta("d15", "24", "44")
        self.cursoEngComputacao.adicionaAresta("d16", "24", "53")
        self.cursoEngComputacao.adicionaAresta("d17", "24", "54")
        self.cursoEngComputacao.adicionaAresta("d18", "24", "72")
        self.cursoEngComputacao.adicionaAresta("d19", "26", "36")
        self.cursoEngComputacao.adicionaAresta("d20", "31", "51")
        self.cursoEngComputacao.adicionaAresta("d21", "31", "52")
        self.cursoEngComputacao.adicionaAresta("d22", "31", "64")
        self.cursoEngComputacao.adicionaAresta("d23", "34", "63")
        self.cursoEngComputacao.adicionaAresta("d24", "35", "63")
        self.cursoEngComputacao.adicionaAresta("d25", "34", "81")
        self.cursoEngComputacao.adicionaAresta("d26", "35", "81")
        self.cursoEngComputacao.adicionaAresta("d27", "36", "44")
        self.cursoEngComputacao.adicionaAresta("d28", "36", "45")
        self.cursoEngComputacao.adicionaAresta("d29", "36", "55")
        self.cursoEngComputacao.adicionaAresta("d30", "43", "62")
        self.cursoEngComputacao.adicionaAresta("d31", "44", "55")
        self.cursoEngComputacao.adicionaAresta("d32", "44", "93")
        self.cursoEngComputacao.adicionaAresta("d33", "45", "93")
        self.cursoEngComputacao.adicionaAresta("d34", "51", "61")
        self.cursoEngComputacao.adicionaAresta("d35", "52", "75")
        self.cursoEngComputacao.adicionaAresta("d36", "54", "81")
        self.cursoEngComputacao.adicionaAresta("d37", "55", "65")
        self.cursoEngComputacao.adicionaAresta("d38", "61", "84")
        self.cursoEngComputacao.adicionaAresta("d39", "61", "94")
        self.cursoEngComputacao.adicionaAresta("d40", "63", "73")
        self.cursoEngComputacao.adicionaAresta("d41", "64", "75")
        self.cursoEngComputacao.adicionaAresta("d42", "64", "84")
        self.cursoEngComputacao.adicionaAresta("d43", "73", "82")
        self.cursoEngComputacao.adicionaAresta("d44", "74", "83")
        self.cursoEngComputacao.adicionaAresta("d45", "75", "85")
        self.cursoEngComputacao.adicionaAresta("d46", "75", "94")
        self.cursoEngComputacao.adicionaAresta("d47", "83", "92")
        self.cursoEngComputacao.adicionaAresta("d48", "92", "103")

        self.cursoTelematica = MeuGrafo([
            '11','12','13','14','15','16','17',
            '21','22','23','24','25','26','27',
            '31','32','33','34','35','36','37',
            '41','42','43','44','45','46','47',
            '51','52','53','54','55','56',
            '61','62','63','64','65'
        ])

        self.cursoTelematica.adicionaAresta('d1', '11', '21')
        self.cursoTelematica.adicionaAresta('d2', '12', '22')
        self.cursoTelematica.adicionaAresta('d3', '16', '22')
        self.cursoTelematica.adicionaAresta('d4', '12', '23')
        self.cursoTelematica.adicionaAresta('d5', '16', '23')
        self.cursoTelematica.adicionaAresta('d6', '13', '24')
        self.cursoTelematica.adicionaAresta('d7', '16', '26')
        self.cursoTelematica.adicionaAresta('d8', '21', '31')
        self.cursoTelematica.adicionaAresta('d9', '26', '32')
        self.cursoTelematica.adicionaAresta('d10', '22', '33')
        self.cursoTelematica.adicionaAresta('d11', '23', '33')
        self.cursoTelematica.adicionaAresta('d12', '26', '33')
        self.cursoTelematica.adicionaAresta('d13', '14', '34')
        self.cursoTelematica.adicionaAresta('d14', '25', '35')
        self.cursoTelematica.adicionaAresta('d15', '21', '36')
        self.cursoTelematica.adicionaAresta('d16', '24', '36')
        self.cursoTelematica.adicionaAresta('d17', '31', '41')
        self.cursoTelematica.adicionaAresta('d18', '31', '42')
        self.cursoTelematica.adicionaAresta('d19', '32', '43')
        self.cursoTelematica.adicionaAresta('d20', '32', '44')
        self.cursoTelematica.adicionaAresta('d21', '33', '44')
        self.cursoTelematica.adicionaAresta('d22', '33', '45')
        self.cursoTelematica.adicionaAresta('d23', '21', '46')
        self.cursoTelematica.adicionaAresta('d24', '34', '46')
        self.cursoTelematica.adicionaAresta('d25', '41', '51')
        self.cursoTelematica.adicionaAresta('d26', '41', '52')
        self.cursoTelematica.adicionaAresta('d27', '44', '53')
        self.cursoTelematica.adicionaAresta('d28', '44', '54')
        self.cursoTelematica.adicionaAresta('d29', '37', '55')
        self.cursoTelematica.adicionaAresta('d30', '41', '55')
        self.cursoTelematica.adicionaAresta('d31', '44', '55')
        self.cursoTelematica.adicionaAresta('d32', '42', '61')
        self.cursoTelematica.adicionaAresta('d33', '51', '61')
        self.cursoTelematica.adicionaAresta('d34', '53', '62')

        self.cursoFisica = MeuGrafo(
        [
            '11', '12', '13', '14', '15', '16', '17',
            '21', '22', '23', '24', '25', '26', '27',
            '31', '32', '33', '34', '35', '36', '37',
            '41', '42', '43', '44', '45', '46',
            '51', '52', '53', '54', '55', '56', '57',
            '61', '62', '63', '64', '65', '66', '68',
            '71', '72', '73', '74', '76',
            '81', '82', '83', '84', '85', '86'
        ]
        )

        self.cursoFisica.adicionaAresta('d1', '11', '21')
        self.cursoFisica.adicionaAresta('d2', '12', '21')
        self.cursoFisica.adicionaAresta('d3', '11', '22')
        self.cursoFisica.adicionaAresta('d4', '12', '22')
        self.cursoFisica.adicionaAresta('d5', '12', '23')
        self.cursoFisica.adicionaAresta('d6', '12', '24')
        self.cursoFisica.adicionaAresta('d7', '14', '24')
        self.cursoFisica.adicionaAresta('d8', '15', '25')
        self.cursoFisica.adicionaAresta('d9', '21', '31')
        self.cursoFisica.adicionaAresta('d10', '23', '31')
        self.cursoFisica.adicionaAresta('d10', '21', '31')
        self.cursoFisica.adicionaAresta('d11', '22', '32')
        self.cursoFisica.adicionaAresta('d12', '23', '33')
        self.cursoFisica.adicionaAresta('d13', '31', '41')
        self.cursoFisica.adicionaAresta('d14', '31', '42')
        self.cursoFisica.adicionaAresta('d15', '32', '42')
        self.cursoFisica.adicionaAresta('d16', '33', '45')
        self.cursoFisica.adicionaAresta('d17', '31', '46')
        self.cursoFisica.adicionaAresta('d18', '41', '51')
        self.cursoFisica.adicionaAresta('d19', '45', '51')
        self.cursoFisica.adicionaAresta('d20', '41', '52')
        self.cursoFisica.adicionaAresta('d21', '42', '52')
        self.cursoFisica.adicionaAresta('d22', '45', '53')
        self.cursoFisica.adicionaAresta('d23', '31', '54')
        self.cursoFisica.adicionaAresta('d24', '43', '55')
        self.cursoFisica.adicionaAresta('d25', '21', '57')
        self.cursoFisica.adicionaAresta('d26', '43', '57')
        self.cursoFisica.adicionaAresta('d27', '51', '61')
        self.cursoFisica.adicionaAresta('d28', '51', '62')
        self.cursoFisica.adicionaAresta('d29', '52', '62')
        self.cursoFisica.adicionaAresta('d30', '21', '63')
        self.cursoFisica.adicionaAresta('d31', '53', '63')
        self.cursoFisica.adicionaAresta('d32', '51', '64')
        self.cursoFisica.adicionaAresta('d33', '56', '66')
        self.cursoFisica.adicionaAresta('d34', '31', '68')
        self.cursoFisica.adicionaAresta('d35', '57', '68')
        self.cursoFisica.adicionaAresta('d36', '61', '71')
        self.cursoFisica.adicionaAresta('d37', '41', '72')
        self.cursoFisica.adicionaAresta('d38', '45', '72')
        self.cursoFisica.adicionaAresta('d39', '66', '73')
        self.cursoFisica.adicionaAresta('d40', '31', '74')
        self.cursoFisica.adicionaAresta('d41', '43', '74')
        self.cursoFisica.adicionaAresta('d51', '41', '76')
        self.cursoFisica.adicionaAresta('d52', '68', '76')
        self.cursoFisica.adicionaAresta('d42', '65', '81')
        self.cursoFisica.adicionaAresta('d43', '74', '82')
        self.cursoFisica.adicionaAresta('d44', '73', '83')
        self.cursoFisica.adicionaAresta('d45', '54', '84')
        self.cursoFisica.adicionaAresta('d46', '71', '84')
        self.cursoFisica.adicionaAresta('d47', '16', '85')
        self.cursoFisica.adicionaAresta('d48', '25', '85')
        self.cursoFisica.adicionaAresta('d49', '51', '86')
        self.cursoFisica.adicionaAresta('d50', '76', '86')

        self.gabaritoMatematica = ['11', '12', '13', '14', '15', '16', '17', '23', '24', '25', '27', '35', '36', '46', '56', '66', '85', '21', '22', '26', '33', '34', '43', '45', '52', '65', '31', '32', '41', '44', '51', '62', '72', '75', '42', '53', '54', '55', '57', '61', '63', '81', '82', '83', '64', '67', '71', '73', '74', '77', '84', '87']
        self.gabaritoConstrucao = ['11', '12', '13', '14', '15', '16', '17', '18', '22', '31', '58', '61', '63', '68', '71', '72', '73', '21', '23', '24', '25', '26', '27', '34', '66', '67', '32', '33', '35', '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', '51', '52', '54', '56', '65']
        self.gabaritoEngenharia = ['11', '12', '13', '14', '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', '91', '101', '102', '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', '43', '53', '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', '55', '61', '75', '82', '93', '65', '84', '85', '94']
        self.gabaritoFisica = ['11', '12', '13', '14', '15', '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', '65', '21', '22', '23', '24', '25', '55', '66', '81', '31', '32', '33', '57', '73', '85', '41', '42', '45', '46', '54', '68', '74', '83', '51', '52', '53', '72', '76', '82', '61', '62', '63', '64', '86', '71', '84']
        self.gabaritoTelematica = ['11', '12', '13', '14', '15', '16', '17', '25', '27', '37', '47', '56', '63', '64', '65', '21', '22', '23', '24', '26', '34', '35', '31', '32', '33', '36', '46', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62']

    def test_kahn(self):
        self.assertListEqual(self.cursoMatematica.kahn(), self.gabaritoMatematica)
        self.assertListEqual(self.cursoConstrEdificios.kahn(), self.gabaritoConstrucao)
        self.assertListEqual(self.cursoEngComputacao.kahn(), self.gabaritoEngenharia)
        self.assertListEqual(self.cursoFisica.kahn(), self.gabaritoFisica)
        self.assertListEqual(self.cursoTelematica.kahn(), self.gabaritoTelematica)

