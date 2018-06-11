""" Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas. """
from random import randint
lista = []
par = []
impar = []
while len(lista) < 20:
    lista.append(randint(1, 100))
for n in lista:
    x = n
    if x % 2 == 0 :
        par.append(x)
    else:
        impar.append(x)
print(lista)
print(par)
print(impar)