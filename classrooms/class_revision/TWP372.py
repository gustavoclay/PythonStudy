from random import randint
secreta = randint(1, 100)
while True:
    chute = int(input('Chute: '))
    if chute == secreta:
        print('Parabés, vc é foda! Acertou o número %d' %secreta)
        break
    else:
        print('Alto' if chute > secreta else 'Baixo')
print('Fim do Jogo')