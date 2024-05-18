# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra

maca=int(input("Digite a quantidade de maças compradas "))
if maca<12:
    soma=maca*1,30
    print("O valor a ser pago é de R$ ",soma)
else:
 soma=maca*1,00
print(" O valor a ser pago é de R$ ",soma)
 