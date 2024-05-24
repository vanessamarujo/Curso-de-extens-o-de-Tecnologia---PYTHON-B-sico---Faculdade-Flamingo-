# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor

valor1=int(input(" Digite o primeiro número : "))
valor2=int(input(" Digite o segundo número : "))
if(valor1>valor2):
 diferenca = valor1-valor2
 print("A diferença entre os valores é:",diferenca)
elif( valor2>valor1):
 diferenca= valor2-valor1
 print(" A diferença entre os valores é: ",diferenca)