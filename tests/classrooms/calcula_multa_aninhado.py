# Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20
# por minuto. Entre 200 e 400 minutos, o preço é R$ 0,18. Acima de 400 minutos o preço por
# minuto é R$ 0,15. Calcule sua conta de telefone

minutos = int(input('Minutos utilizados: '))
if minutos < 200 :
    preco = 0.20
else:
    if minutos <= 400:
        preco = 0.18
    else:
        preco = 0.15
print('Valor da Conta: R$%6.2f' % (minutos * preco))
