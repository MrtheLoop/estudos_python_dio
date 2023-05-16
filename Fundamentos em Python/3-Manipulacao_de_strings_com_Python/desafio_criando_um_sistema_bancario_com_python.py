menu_principal = """
========= MENU ==========
[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair

Digite uma opção: 
"""

menu_pos_operacao = """

======== MENU PÓS OPERAÇÃO ========
    Você quer fazer outra operação?

[S] Sim
[N] Não

:
"""

saldo = 2000.00
quantidade_saque = 0
LIMITE_SAQUE = 3
opcao = -1
opcao1 = -1

while opcao != 0:

    opcao = int(input(menu_principal))

    if opcao == 1:
        valor_depositado = int(input("Insira o valor que deseja depositar: "))
        print("Calculando valor depoistado...")
        print(f"Valor deposito com sucesso. Seu saldo atual é de R${saldo + valor_depositado}")
        opcao1 = (input(menu_pos_operacao))

        if opcao1 =="S":
            print(opcao)

        elif opcao1 == "N":
            break

        else:
            print("Opção inválida! Verifique o menu e tente novamente.")
            break


    if opcao == 2:
        valor = int(input("Digite o valor que deseja sacar: "))
        print(f"Saque realizado. Seu saldo agora é de {saldo - valor}")
        print(opcao1)
        

else:
    print("Opção inválida! Verifique o menu e tente")