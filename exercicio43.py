# Curso Básico de PYTHON
# Nome da desenvolvedora: Vanessa Marujo Nogueira
# Versão 1.0
# Exercício de lógica de programação com a linguagem de programação PYTHON
# Exercício Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever 
# o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever 
# a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'

conta=int(input("Informe o número da conta: "))
saldo=float(input("Informe o saldo: "))     
debito=float(input("Informe o débito : ")) 
credito=float(input("Informe o crédito : "))  
saldo_atual = (saldo - debito + credito)
   
if saldo_atual >= 0 :   
        print("Saldo positivo,seu saldo é de R$ ",saldo_atual)   
else:     
        print ("Saldo negativo, seu saldo é de R$ ",saldo_atual) 