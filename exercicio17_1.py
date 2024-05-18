# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Cálculo do produto

valorDoProduto=float(input(" Digite o valor do produto :"))
valorDesconto=float(input(" Digite o percentual de desconto"))
valorFinal=valorDoProduto - (valorDoProduto * (valorDesconto/100))
print(" O valor do produto final é : ",valorFinal)
