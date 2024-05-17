# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Digite uma frase e conte as vogais

palavra = input("Digite uma palavra ou frase: ")
contador_vogais = 0
vogais = ['a', 'e', 'i', 'o', 'u']
for caractere in palavra:
 if caractere.lower()in vogais:
  contador_vogais+= 1
print("A palavra ou frase possui", contador_vogais, "vogais.")








