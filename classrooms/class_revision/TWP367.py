'''Sortear um numero para o jogo do advinho'''
from random import randint
print('Bem Vindo!')
chute = 0
sorteado = randint(1, 100)
while chute != sorteado:
    g = input('Chute um numero: ')
    chute = int(g)
    if chute == sorteado:
        print('Você venceu!')
    else:
        if chute > sorteado:
            print('Alto')
        else:
            print('Baixo')
print('Fim do jogo')