'''Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))
'''
if a != b and b != c and c != a:
    print ('Triângulo escaleno')
else:
    if a == b or b == c or c == a:
        print('Triângulo isósceles')
        else:
            print('Triângulo equilátero')
'''
if a != b:
    if b != c and c != a:
        print ('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    if b != c:
        print('Triângulo isósceles')
    else:
        print('Triângulo equilátero')
