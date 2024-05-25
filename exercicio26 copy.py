# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Digite um número e verifique se é primo ou não

numero =int(input("Digite um número inteiro para saber se é primo :"))

if numero<=1:

    print("O número não é primo")

elif numero%2==0 and numero!=2:

    print("O número não é primo")

elif numero%3==0 and numero!=3 or numero%5==0 and numero!=5 or numero%7==0 and numero!=7:

  print("O número não é primo")

else:

    print("O número é primo")

