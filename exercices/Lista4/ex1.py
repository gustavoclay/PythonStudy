"""1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min."""
from random import randint
lista = []
while len(lista) < 10:
    x = randint(10, 100)
    lista.append(x)
print(lista)
temp = 0
for item in range(1, 10):
    if lista[item] > temp:
        temp = lista[item]
print('Maior ', temp)