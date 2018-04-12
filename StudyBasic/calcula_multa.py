# Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110km/h,
# exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa
# cobrando 5,00 R$ por km acima de 110.

velocidade = int(input('Velocidade: '))
if velocidade <= 3:
    print ('Velocidade permitida!')
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print ('Velocidade acima do permitido. Você foi multado em %.2f R$!' %multa)
    
