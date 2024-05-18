# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Digite três números e retorne o maior deles

a=int(input("Digite o primeiro número : "))
b=int(input("Digite o segundo número : "))
c=int(input("Digite o terceiro número : "))
if ((a>b)&(a>c)):
    print(" O maior número digitado é :",a)
elif ((b>a)&(b>c)):
    print(" O maior número digitado é :",b)
else:
    print(" O maior número digitado é :",c)