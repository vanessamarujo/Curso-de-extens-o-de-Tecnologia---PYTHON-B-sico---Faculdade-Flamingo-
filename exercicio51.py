# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Efetuar a leitura de três valores (variáveis A, B e C) e 
# apresentá-los dispostos em ordem crescente

a=int(input("Digite a variável A: "))
b=int(input("Digite a variável B: "))
c=int(input("Digite a varíavel C: "))
if a >= b and a >= c and b >= c:
    print(f'A ordem crescente é {c} , {b} e {a}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem crescente é {b} , {c} e {a}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem crescente é {c} , {a} e {b}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem crescente é {a} , {c} e {b}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem crescente é {b} , {a} e {c}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem crescente é {a} , {b} e {c}')