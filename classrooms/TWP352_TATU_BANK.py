# Classes e Objetos - Informatizar o banco TATU
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
    def resumo(self):
        print('CC numero: %s Saldo: %10.2f' %(self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self -= valor
    def deposito(self, valor):
        self.saldo += valor