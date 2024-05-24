# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Ler quatro valores referentes a quatro notas escolares de um aluno 
# e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar
# for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando 
# esta condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição

print ("Programa para cálculo de média de sua nota")
nota1 =int (input("Digite a primeira nota : "))
nota2 =int (input("Digite a segunda nota : "))
nota3 =int (input("Digite a terceira nota : "))
nota4 =int (input("Digite a quarta nota : "))
media = (nota1+nota2+nota3+nota4)/4
if media>=5:
 print ("Você foi APROVADO,sua nota média é : ",media)
elif media<5:
 print("Você foi REPROVADO,sua nota média é : ",media)
