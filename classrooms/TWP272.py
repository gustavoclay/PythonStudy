'''Faça um programa que leia um vetor de dez números reais e mostre-os na ordem inversa'''
vetor = []
i = 1
while i <= 10:
    n = float(input("Digite um numero real:"))
    vetor.append(n)
    i += 1
i = 9
while i >= 0:
    print(vetor[i])
    i -= 1
