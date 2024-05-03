menu = """
============MENU============


[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair


============================
=>"""

saldo = 0
limete = 500
extrato = ""
numero_de_saques = 0
LIMETE_SAQUES = 3
operacao = "desculpa, mais essa opisao nao exite obrigado =)"
while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Digite o valor que o senhor ou senhar quer depositar: "  "R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print(operacao)

    
    elif opcao == "S":
        valor = float(input("Digite o valor do saque: R$"))

        exedou_o_saldo = valor > saldo

        exedou_o_limete = valor > limete

        exedou_o_limete_de_saque = numero_de_saques >= LIMETE_SAQUES

        if exedou_o_saldo:
            print("operacao invalida, Voce nao tem saldo suficiente.")
        if exedou_o_limete:
            print("vc so pode sacar R$500 por saque.")
        if exedou_o_limete_de_saque:
            print("vc so pode sacar 3 vezes, volte amanha para sacar mais")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print(operacao)
    elif opcao == "E":
        print("\n============ EXTRATO ============")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")
    elif opcao == "Q":
        break
    else:
        print(operacao)
