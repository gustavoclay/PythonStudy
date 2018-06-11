''' Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores. '''
from random import randint
lista_a = []
lista_b = []
lista_c = []
while len(lista_a) < 10:
    lista_a.append(randint(1, 100))
    lista_b.append(randint(1, 100))
for n in range(1, 20):
    lista_c.append(lista_a[])