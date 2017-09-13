from conta import Conta


class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, numero_conta, saldo_inicial):
        conta = Conta(numero_conta, saldo_inicial)
        self.contas.append(conta)

    def debitar(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        conta.debitar(valor)

    def creditar(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        conta.creditar(valor)

    def transferir(self, conta_origem, conta_destino, valor):
        origem = self.buscar_conta(conta_origem)
        destino = self.buscar_conta(conta_destino)
        origem.transferir(valor, destino)

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta

    def mostrar_conta(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        print('Numero:', conta.numero, 'Saldo:', conta.get_saldo())

    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Debitar')
        print('3 - Creditar')
        print('4 - Transferir')
        print('5 - Mostrar conta')
        print('x - Sair')
        opcao = input('Digite a opção:')

        if opcao == '1':
            numero_conta = input('Digite o número:')
            self.cadastrar_conta(numero_conta, 0)
        if opcao == '2':
            numero_conta = input('Conta:')
            valor = float(input('Valor:'))
            self.debitar(numero_conta, valor)
        if opcao == '3':
            numero_conta = input('Conta:')
            valor = float(input('Valor:'))
            self.creditar(numero_conta, valor)
        if opcao == '4':
            conta_origem = input('Conta Origem:')
            conta_destino = input('Conta Destino:')
            valor = float(input('Valor:'))
            self.transferir(conta_origem, conta_destino, valor)
        if opcao == '5':
            numero_conta = input('Conta:')
            self.mostrar_conta(numero_conta)

        return opcao