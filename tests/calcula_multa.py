# Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20
# por minuto. Entre 200 e 400 minutos, o preço é R$ 0,18. Acima de 400 minutos o preço por
# minuto é R$ 0,15. Calcule sua conta de telefone

minutos = int(input('Minutos utilizados: '))
if minutos < 200 :
    print('Valor da conta:', minutos * 0.20)
if minutos >= 200 and minutos <= 400:
    print('Valor da conta:', minutos * 0.18)
if minutos > 400:
    print('Valor da conta:', minutos * 0.15)
