menu = """
[1] Depositar
[2] Sacar
[3] Extrato 
[0] Sair

=> """

saldo = 0 
limite = 500 
extrato = ""
numero_saques = 0 
LIMITE_SAQUE = 3

while True: 
    opcao = input(menu)

    if opcao == "1": 
        valor = float(input("Informe o valor do depósito: "))
        resultado_saldo_extrato = deposito(saldo, valor, extrato)
        saldo = resultado_saldo_extrato[saldo]
        extrato = resultado_saldo_extrato[extrato]
        
#         if valor > 0: 
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"
        
#         else: 
#             print("Operação falhou! O valor informado é inválido. ")

#     elif opcao == "2":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = valor > numero_saques >= LIMITE_SAQUE

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente. ")

#         elif excedeu_limite: 
#             print("Operação falhou! O valor do saque excede o limite. ")

#         elif excedeu_saques: 
#             print("Operação falhou! Número máximo de saques excedidos. ")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido. ")
    
#     elif opcao == "3": 
#         print("\n=============EXTRATO=============")
#         print("Não foram realizados movimentações." if not extrato else extrato) 
#         print(f"\nSaldo: R$ {saldo:.2f}\n")
#         print("==================================")

#     elif opcao == "0": 
#         break


    def deposito(saldo, valor, extrato): 
        saldo_extrato = {saldo: 0, extrato: ""}

        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            saldo_extrato[saldo] = saldo
            saldo_extrato[extrato] = extrato
            
            
        else: 
            print("Operação falhou! O valor informado é inválido. ")

        return saldo_extrato
    
    def saque(numero_saque):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = valor > numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")

        elif excedeu_limite: 
            print("Operação falhou! O valor do saque excede o limite. ")

        elif excedeu_saques: 
            print("Operação falhou! Número máximo de saques excedidos. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido. ")

    def extrato(): 
        print("\n=============EXTRATO=============")
        print("Não foram realizados movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("==================================")

