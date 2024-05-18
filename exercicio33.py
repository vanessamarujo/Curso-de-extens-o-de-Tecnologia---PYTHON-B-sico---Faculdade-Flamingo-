# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
# Calcular e escrever o valor do novo salário.

salario=float(input(" Digite o seu salário : "))
percentual=float(input(" Digite o percentual de reajuste : "))
percentual =percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
print('Aumento: R$ ',aumento)
print(" Seu novo salário é R$",novo_salario)
