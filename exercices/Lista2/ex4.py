'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if (n1 > n2 and n1 > n3):
    print("Maior: $d", n1)
elif (n2 > n1 and n2 > n3):
    print("Maior: $d", n2)
else:
    print("Maior: $d", n3)
    