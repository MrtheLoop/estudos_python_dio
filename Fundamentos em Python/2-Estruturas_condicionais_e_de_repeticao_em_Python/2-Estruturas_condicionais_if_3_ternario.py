# If ternário

# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira é o retorno caso a expressã
# retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

# Ex:

saldo = 2000.00
saque = 1500.00

status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque") 