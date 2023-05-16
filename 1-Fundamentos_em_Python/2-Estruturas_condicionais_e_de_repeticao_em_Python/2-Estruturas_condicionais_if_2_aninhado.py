# If aninhado

# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco 
# de código de estruturas if/elif/else

# Basicamente é um if dentro de outro if

#Ex: 

conta_normal = True
conta_universitaria = False
saldo = 2000.00
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
elif saque <= (saldo + cheque_especial):
              print("Saque realizado com uso de cheque especial!")
elif conta_universitaria:
       if saldo >= saque:
              print("Saque realizado com sucesso!")
       else:
              print("Saldo insuficiente")

            