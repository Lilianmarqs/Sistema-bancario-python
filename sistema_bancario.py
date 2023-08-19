import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
        
def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato 
    [4] Nova Conta
    [5] Listar Conta
    [6] Novo usuário 
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.valor
        excedeu_saldo =  valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")

        elif valor > 0:
            self._saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("\n Saque realizado com sucesso! ")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido. ")

        return False
        

    def depositar(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso! ")

        else: 
            print("Operação falhou! O valor informado é inválido. ")
            return False
        
        return True 


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]) #<- comprensão de lista
         
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques


        if excedeu_limite: 
            print("Operação falhou! O valor do saque excede o limite. ")

        elif excedeu_saques: 
            print("Operação falhou! Número máximo de saques excedidos. ")

        else:
            super().sacar(valor)
    
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes=[]
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adcionar_transacao(self, transacao):
        self._transacoes.append(  # <- a transação é armazenado na lista como um dicionárop
            { #<- dicionário
                "tipo": transacao._class_._name_, #será armazenado no dicionário o nome da transaçao(saque ou deposito), 
                "valor":  transacao.valor, #o valor da transaçao,
                "data": datetime.now().strtime("%d-%m-%Y %H:%M:%s"), #e a data que ela foi feita
            }
        )
     
class Transacao(ABC): 
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): 
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adcionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self): 
        return self._valor
    
    def registrar(self, conta): 
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente: #deixei essa opção pronta pra entender melhor as demais
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):  #metodo realizar_transacao que recebe dois atributos: conta, transacao
        transacao.registrar(conta)

    def adcionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        data_nascimento = data_nascimento

def deposito(saldo, valor, extrato, /): 
    if valor > 0: 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso! ")

    else: 
        print("Operação falhou! O valor informado é inválido. ")

    return saldo, extrato

# def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

#     excedeu_saldo = valor > saldo

#     excedeu_limite = valor > limite

#     excedeu_saques = valor > numero_saques >= limite_saques

#     if excedeu_saldo:
#         print("Operação falhou! Você não tem saldo suficiente. ")

#     elif excedeu_limite: 
#         print("Operação falhou! O valor do saque excede o limite. ")

#     elif excedeu_saques: 
#         print("Operação falhou! Número máximo de saques excedidos. ")

#     elif valor > 0:
#         saldo -= valor
#         extrato += f"Saque: R$ {valor:.2f}\n"
#         numero_saques += 1
#         print("\n Saque realizado com sucesso! ")

#     else:
#         print("Operação falhou! O valor informado é inválido. ")

#     return saldo, extrato

# def exibir_extrato(saldo, /, *, extrato): 
#     print("\n=============EXTRATO=============")
#     print("Não foram realizados movimentações." if not extrato else extrato) 
#     print(f"\nSaldo: R$ {saldo:.2f}\n")
#     print("==================================")

# def criar_usuario(usuarios):
#     cpf = input("Informe o CPF (somente número): ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n@@@ Já existe usuário com esse CPF! @@@")
#         return

#     nome = input("Informe o nome completo: ")
#     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
#     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

#     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

#     print("=== Usuário criado com sucesso! ===")

# def filtrar_usuario(cpf, usuarios):
#     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#     return usuarios_filtrados[0] if usuarios_filtrados else None

# def criar_conta(agencia, numero_conta, usuarios):
#     cpf = input("Informe o CPF do usuário: ")
#     usuario = filtrar_usuario(cpf, usuarios)

#     if usuario:
#         print("\n=== Conta criada com sucesso! ===")
#         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

#     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

# def listar_contas(contas):
#     for conta in contas:
#         linha = f"""\
#             Agência:\t{conta['agencia']}
#             C/C:\t\t{conta['numero_conta']}
#             Titular:\t{conta['usuario']['nome']}
#         """
#         print("=" * 100)
#         print(textwrap.dedent(linha))

# def main():
#     LIMITE_SAQUES = 3
#     AGENCIA = "0001"

#     saldo = 0
#     limite = 500
#     extrato = ""
#     numero_saques = 0
#     usuarios = []
#     contas = []

#     while True:
#         opcao = menu()

#         if opcao == "1":
#             valor = float(input("Informe o valor do depósito: "))

#             saldo, extrato = deposito(saldo, valor, extrato)

#         elif opcao == "2":
#             valor = float(input("Informe o valor do saque: "))

#             saldo, extrato = saque(
#                 saldo=saldo,
#                 valor=valor,
#                 extrato=extrato,
#                 limite=limite,
#                 numero_saques=numero_saques,
#                 limite_saques=LIMITE_SAQUES,
#             )

#         elif opcao == "3":
#             exibir_extrato(saldo, extrato=extrato)

#         elif opcao == "4":
#             criar_usuario(usuarios)

#         elif opcao == "5":
#             numero_conta = len(contas) + 1
#             conta = criar_conta(AGENCIA, numero_conta, usuarios)

#             if conta:
#                 contas.append(conta)

#         elif opcao == "6":
#             listar_contas(contas)

#         elif opcao == "0":
#             break

#         else:
#             print("Operação inválida, por favor selecione novamente a operação desejada.")


# main()