# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício de Cálculo do produto

print("Programa para Cálculo do valor do produto com desconto aplicado")
preco = float(input("Digite o preço da mercadoria: R$ "))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = preco * desconto / 100
a_pagar = preco - valor_do_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preco))
print("vale R$ %7.2f." % valor_do_desconto)
print("O valor a pagar é de R$ %7.2f" % a_pagar)
