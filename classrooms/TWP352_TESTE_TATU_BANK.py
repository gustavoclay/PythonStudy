from TWP352_TATU_BANK import Cliente
from TWP352_TATU_BANK import Conta
joao = Cliente('João Da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-1234')
print('Nome: %s. Telefone: %s.' %(joao.nome, joao.telefone))
print('Nome: %s. Telefone: %s.' %(maria.nome, maria.telefone))
conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria], 2, 500)
conta1.resumo()
conta2.resumo()