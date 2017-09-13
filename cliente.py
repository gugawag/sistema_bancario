class Cliente():

    def __init__(self, nome='', cpf=''):
        self.nome = nome
        self.cpf = cpf
        self.idade = 20

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade= idade