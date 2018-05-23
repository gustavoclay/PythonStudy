'''
    Comentários de várias linhas com três aspas
    Faça um programa que leia 3 números e mostre o maior deles.
'''
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

if a >= b and a >=c:
    print('Maior: Primeiro: ', a)
elif b >= c:
    print('Maior: Segundo: ', b)
else:
    print('Maior: Terceiro:',  c)