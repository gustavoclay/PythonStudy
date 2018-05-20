'''Faça um programa que leia quatro notas, mostre as notas e a media na tela'''
vetor = []
i = 1
media = 0
while i <= 4:
    n = float(input("Digite um numero:"))
    vetor.append(n)
    i += 1
    media += n
print("Notas: ", vetor, ". Media:", media/len(vetor))