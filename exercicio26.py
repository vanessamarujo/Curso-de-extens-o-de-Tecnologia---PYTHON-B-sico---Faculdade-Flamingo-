# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Digite um número e verifique se é primo ou não


number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print('É um número primo')
else:
  print('Não é um número primo')