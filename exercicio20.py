# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Hexagono
# Importação da biblioteca Math

import math
lado= float(input("Digite o valor do lado de um hexagono para calculo da area : "))
resultado= ((3*pow(lado,2)*math.sqrt(3))/2)
print ("A área do hexagono é : ", round(resultado,2), "m²")