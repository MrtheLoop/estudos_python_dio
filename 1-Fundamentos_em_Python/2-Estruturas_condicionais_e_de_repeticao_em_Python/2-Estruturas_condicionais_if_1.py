# If / if-else / elif

#O que são?

# A estrutura condicional permite o desvio de controle, quando determinadas expressões lógicas são atendidas

#if

# Para criar uma estrutura condicional simples, composta por um unico desvio, podmos utilizar
# a palavra reservada if. O comando irá testar a expressão lógica, 
# e em caso de retoro verdadeiro as ações presetes no vloco de código do if serão executadas

# Ex:

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
    
#If/Else

# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else
# Como sabemos, se a expressão lógica testada no if for verdadeira, então o bloco de código do if será 
# executada. Caso contrário o bloco de código do else será executado.

# Ex:

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
    
else:
    print("Saldo insuficiente!")
    
# if / elif / else

# Em alguns cenários queremos mais de dois desvios,, para isso podemos utilizar a palavra reservada elif.
# O elif é composto por uma nova lógica, que serpa testada e caso retorne verdadeiro o bloco de código
# do elif será executado. Não existe um grande número máximo de elifs que podemos utilizar,
# porém evite criar grandes estruturas condicionais pois elas aumentam a complexidade do código.

opcao = int(input("Informe uma opção: [1] saca \n [2] Extrato"))
if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
    #...
elif opcao == 2:
    print("Exibindo o extrato...")
#else:
#    sys.exit("Opção inválida")
    
# If Aninhado
# If Ternário