'''Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.'''
a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
r = 0
while a % b != 0:
    a, b = b, a % b
print ("MDC: ", b)