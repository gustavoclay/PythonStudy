#Calcule o fatorial de n
n = int(input('Digite um numero:'))
i = 1
fat = 1
while i <= n:
    fat = fat * i
    i = i + 1
print ('Fatorial', fat)