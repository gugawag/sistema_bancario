class Conta:
    """Representa uma Conta bancária. Conta simplificada por questões didáticas."""

    def __init__(self, numero='', saldo=0):
        self.numero = numero
        self.saldo = saldo

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def transferir(self, valor, destino):
        self.debitar(valor)
        destino.creditar(valor)

    def get_saldo(self):
        return self.saldo
