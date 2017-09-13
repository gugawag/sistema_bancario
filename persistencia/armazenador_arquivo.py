# Author: Gustavo Wagner, gugawag@gmail.com
import json
from conta import Conta
from cliente import Cliente


class ArmazenadorArquivo:
    def __init__(self, arquivo_clientes = 'clientes.txt', arquivo_contas = 'contas.txt'):
        self.arquivo_clientes = arquivo_clientes
        self.arquivo_contas = arquivo_contas

    def salvar_clientes(self, clientes):
        fClientes = open(self.arquivo_clientes, 'w')
        json_string = json.dumps([cliente.__dict__ for cliente in clientes])
        fClientes.write(json_string)
        fClientes.close()

    def salvar_contas(self, contas):
        fContas = open(self.arquivo_contas, 'w')
        json_string = json.dumps([conta.__dict__ for conta in contas])
        fContas.write(json_string)
        fContas.close()

    def carregar_clientes(self):
        fClientes = open(self.arquivo_clientes, 'r')
        strClientes = ''

        for linha in fClientes.readline():
            strClientes += linha

        clientes = list()
        for clienteJson in json.loads(strClientes):
            cliente = Cliente()
            for coluna in clienteJson.keys():
                cliente.__dict__[coluna] = clienteJson[coluna]
            clientes.append(cliente)
        return clientes

    def carregar_contas(self):
        fContas = open(self.arquivo_contas, 'r')

        str_contas = ''

        for linha in fContas.readline():
            str_contas += linha

        contas = list()
        for conta_json in json.loads(str_contas):
            conta = Conta()
            for coluna in conta_json.keys():
                conta.__dict__[coluna] = conta_json[coluna]
            contas.append(conta)
        return contas
