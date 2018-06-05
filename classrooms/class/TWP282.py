'''Faça um programa que leia uma palavra e troque as vogais por "*" '''
palavra = input("Digite uma palavra:")
texto = ''
i = 0
while i < len(palavra):
    if palavra[i] in 'aeiou':
        texto += '*'
    else:
        texto += palavra[i]
    i += 1
print("Resultado: ", texto)