'''
Gerar uma lista de 15 numeros inteiros aleatórios entre 10 e 100
'''
import random
lista = []
for k in range(15):
    lista.append(random.randint(10, 100))
print (lista)