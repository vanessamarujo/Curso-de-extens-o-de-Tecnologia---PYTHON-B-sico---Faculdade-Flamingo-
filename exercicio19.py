# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de transformação de dias, horas e minutos para segundos

print ("Programa de transformação de dias, horas e minutos para segundos")
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print('O valor total em segundos é de %ds.' % total)