# Fatiamento de string

# Fatiamento de strings é uma técnica utilizada para retornar substrings (parte da string original), informando
# inicio (start), fim (stop) e passo (step); [start:stop[,step]]

# fatiamento:

nome = "Guilherme Arthur de Carvalho"

nome[0]
#>>>G

nome [:9]
#>>> "Guilherme"

nome[10:]
#>>>"Arthur de Carvalho"

nome[10:16]
#>>> "Arthur"

nome[10:16:2]
#>>>"Atu"

nome[:]
#>>>"Guilherme Arthur de Carvalho"

print(nome[::-1])
#>>>"ohlavraC ed ruhtrA emrehliuG"