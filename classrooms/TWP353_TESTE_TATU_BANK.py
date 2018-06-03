from TWP353_TATU_BANK2 import Cliente
from TWP353_TATU_BANK2 import Conta
joao = Cliente('João da Silva', '775-1234')
maria = Cliente('Maria da Silva', '775-65432')
conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.saque(50)
conta2.deposito(3000)
conta1.saque(190)
conta2.saque(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()