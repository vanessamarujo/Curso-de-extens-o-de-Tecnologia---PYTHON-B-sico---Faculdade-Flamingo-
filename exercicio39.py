# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício  Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem
# que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também
# a média calculada.

nota1=int(input("Digite a nota da 1º avaliação"))
nota2=int(input("Digite a nota da segunda avaliação"))
media= (nota1+nota2)/2
print(" Sua média foi",media)
if media>=6:
 (print (" Você foi APROVADO, sua nota é: ",media))
else:
 print(" Você foi REPROVADO, sua nota é :", media)