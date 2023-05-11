# O que são estruturas de reptição

#São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido 
# previamente ou determinado através de uma expressão lógica.

# Exemplo sem repetição

# Receba umnúmero do teclado e exia os 2 números seguintes

# a = int(input("Informe um número inteiro: "))
# a += 1
# print(a)

# a += 1
# print(a)


# Exemplo com repetição

#Receba um número do teclado e exiba os 2 números seguintes

# ATENÇÃO: O código abaixo não possui sintaxe de Python, é um exemplo.

# a = int(input("Informe um número inteiro: "))
# print(a)

# ~Comando For

# Ocomando -for- é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número 
# exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer 
# um objeto iterável

# Objeto iterável: é definido como um objeto capaz de retornar seus membros um de cada vez

# For
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra,end="")
# print() #adiciona uma quebra de linha

# Função range

# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros
# a partir de um início(inclusive) para um fim(exclusivo). Se usarmos range (i, j) será produzido 

# i, i+1 i+2, i+3, ..., j-1...

# Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step(opcional)


#range

#range(stop) -> range objetc
#range(start,stop[, step]) -> range object

list(range(4))
#>>> [0, 1, 2, 3]


#utilizando range com for

for numero in range (0,11):
    print(numero,end="")

#>>>1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#Exibindo tabuada do 5

for numero in range (0, 51, 5):
    print(numero, end="")

#>>> 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

# O end="" serve para forçar os caracteres a ficar um do lado do outro

# Comando While

# O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while
# quando não sabemoso número de vezes que nosso bloco de código deve ser executado


#while

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")