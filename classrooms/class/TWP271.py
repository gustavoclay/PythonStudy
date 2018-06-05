'''Faça um programa que leia um vetor de 5 números inteiros e mostre o valor'''
vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um número:"))
    vetor.append(n)
    i += 1
print(vetor)