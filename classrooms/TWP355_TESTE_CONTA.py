from TWP355_CONTA_ESPECIAL import Cliente
from TWP355_CONTA_ESPECIAL import Conta, ContaEspecial
joao = Cliente('João da Silva', '775-1234')
maria = Cliente('Maria da Silva', '775-65432')
conta1 = Conta([joao], 1, 1000)
conta2 = ContaEspecial([maria, joao], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()