"""1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min."""
from random import randint
lista = []
while len(lista) < 10:
    x = randint(10, 100)
    lista.append(x)
print(lista)
temp = 0
for n in lista:
    if lista[n] > temp:
        temp = lista[n]
print('Maior ', temp)