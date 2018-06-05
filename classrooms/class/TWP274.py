'''Faça um programa que leia um vetor com 10 caracteres minúsculos e diga quantas consoantes foram lidas'''
letras = []
i = 1
while i <= 10:
    l = str(input("Digite uma letra:"))
    letras.append(l)
    i += 1
i = 0
count = 0
while i <= 9: 
    if letras[i] not in 'aeiou':
        count += 1
    i += 1
print ("Quantidade de consoantes lidas: ", count)