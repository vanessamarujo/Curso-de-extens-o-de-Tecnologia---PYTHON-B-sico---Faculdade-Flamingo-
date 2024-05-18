# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores

eleitores=int(input("Digite o número total de eleitores :"))
branco=int(input("Digite o total de votos em branco : "))
nulos=int(input("Digite o total de votos nulos : "))
validos=int(input("Digite o total de votos válidos : "))
percentual_votosbrancos = (branco/eleitores)*100
percentual_votosnulos = (nulos/eleitores)*100
percentual_votosvalidos = (validos/eleitores)*100
print('Temos um total de {} eleitores.\n {}% são votos brancos.\n {}% são votos nulos.\n {}% são votos validos.'.format(eleitores, percentual_votosbrancos, percentual_votosnulos, percentual_votosvalidos))

