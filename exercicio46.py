# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

valor=int(input(" Digite um valor que deseja saber a tabuada: "))
contadora=1
while contadora <= 10:
    print(valor,"X", contadora,"=",valor*contadora)
    contadora+=1