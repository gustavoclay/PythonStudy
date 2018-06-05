print('Bem Vindo!')
g = input('Chute um numero: ')
Chute = int(g)
if Chute == 42:
    print('Você venceu!')
elif Chute > 42:
    print('Alto')
elif Chute < 42:
    print('Baixo')
print('Fim do jogo')