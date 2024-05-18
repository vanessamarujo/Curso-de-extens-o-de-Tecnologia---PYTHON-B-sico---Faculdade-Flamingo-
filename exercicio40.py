# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar
# este ano (não é necessário considerar o mês em que a pessoa nasceu).

nascimento=int(input(" Digite o ano do seu nascimento "))
nascimento= 2024-nascimento
if nascimento>=18:
     print(" Você pode votar, sua idade atual é :",nascimento)
else:
    print("Você Não poderá votar, sua idade atual é : ",nascimento)