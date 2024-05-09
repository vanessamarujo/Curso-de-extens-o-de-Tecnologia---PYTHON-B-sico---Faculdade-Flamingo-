# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Hexagono


import math
print ("Programa de dimensões de um Hexagono")
Lado = int(input('Insira o valor do lado(m): '))    
area = ((6 *(Lado * Lado *math.sqrt (3))) / 4)
print(f'A Área é igual a {area} m^2')
