# O que são? 

# São operadores utilizados em conjunto com os operdaores de comparação, para montar uma expressão lógica.
# Quando um operador de comparação é utilizado, o resultado retornado é booleano, dessa forma podemos combinar operadores de comparação
# com os operadores lógicos
#Ex:
# op_comparacao + op_logico + op_comparacao...N...

#Ex:

saldo = 1000
saque = 200
limite = 100

saldo >= saque
#>>>True

saque <= limite
#>>>False

# Operador E

saldo = 1000
saque = 200
limite = 100

saldo + saque and saque <= limite
#>>>False

# Operador OU

saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
#>>>True


# Operador de negação
contatos_emergencia = []
not 1000 > 1500
#>>>True

not contatos_emergencia
#>>>True

not "saque 1500;"
#>>>False

not ""
#>>>True

#O operdaor de negação basicamene inverte o valor, então ele diz
# não 1000 > 1500, ok? Aí o compilador diz: verdade, 1000 não é maior que 1500

# Parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saque >= saque
#>>>True

(saldo >= saque and saque <= limite) or (conta_especial and saque >= saque)

# lógica Booleana

# AND = as duas condições precisam ser verdadeiras pra ser True 
# True and True = True 
# True and False = False
# OR = Apenas uma das condições precisam ser verdadeiras
# True or True = True
# True or False = True 