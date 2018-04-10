# 9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
p = int(input('KM percorridos: '))
d = int(input('Quantidade de Dias: '))

print ('Valor a Pagar: ', float ((d * 60) + (p * 0.15)))
