# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar 
# o número lido como sendo um valor positivo, ou seja, o programa deverá apresentar 
# o módulo de um número fornecido. Lembre-se de verificar se o número fornecido é 
# menor que zero; sendo, multiplique-o por -1.

numero=int(input(" Digite um número: "))
if(numero<0):
 resultado= numero*(-1)
 print(" O resultado é : ", resultado)
elif (numero>0): 
 print(" O resultado é : ",numero)
 