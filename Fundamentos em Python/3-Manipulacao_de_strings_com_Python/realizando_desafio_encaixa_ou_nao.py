# Função para verificar se B encaixa em A
def verifica_encaixe(A, B):
    # Verificar se os últimos dígitos de A são iguais a B
    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Ler a quantidade de casos de teste
N = int(input())

# Processar cada caso de teste
for _ in range(N):
    # Ler os valores A e B
    A, B = input().split()

    # Chamar a função para verificar o encaixe e imprimir o resultado
    resultado = verifica_encaixe(A, B)
    print(resultado)