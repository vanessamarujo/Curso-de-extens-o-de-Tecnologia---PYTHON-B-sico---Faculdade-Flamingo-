# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)

contadora=1
acumuladora=0
while(contadora<101):
    acumuladora= acumuladora + contadora
    contadora+=1

print(" A Soma total corresponde: ",acumuladora)
