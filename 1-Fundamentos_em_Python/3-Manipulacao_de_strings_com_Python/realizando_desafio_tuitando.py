''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''

#Código abaixo foi sem pesquisa
#T = int(input(""" """))
#if T <= int(140):
#    print("TWEET")      
#else:
#    print("MUTE")
    
#Resultado: 1 teste passado de 2 testes.

#Teste abaixo realizado com pesquisa, porém sem pesquisar resposta e sim pesquisando método de leitura de caracteres

T = input("Digite aqui o texto: ")

U = len(T)

if U <= int(140):
   print("TWEET")

else:
   print("MUTE")   
   
#Resultado: Código aprovado, usando o len() para ler os caracteres