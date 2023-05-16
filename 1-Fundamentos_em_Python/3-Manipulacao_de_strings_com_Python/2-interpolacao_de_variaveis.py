# Interpolação de variáveis

# Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format
# e a última é utilizando o f strings
# A primeira forma não é atualmente recomendada e seu uso em python 3 é raro, por esse motivo iremos focar nas 2 últimas

# Ex:

# Old Style

nome = "Matheus"
idade = 21
profissao = "programador"
linguagem = "Python"
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))


#Método format

nome = "Matheus"
idade = 21
profissao = "programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

# Note que o exemplo acima é idêntico ao método ol style, por isso foi implementado as funções do próximo exemplo

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(nome, idade, profissao, linguagem))

#print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format{nome=nome, idade=idade, profissao=profissao, linguagem=linguagem})

#print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))

# f-string

nome = "Matheus"
idade = 21
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")

#Formatar strings com f-string

PI = 3.14159

print(f"valor de PI: {PI:.2d}")
#>>> "valor de PI: 3.14"

print(f"valor de PI: {PI: 10.2f}")
#>>> "valor de PI:      3.14"