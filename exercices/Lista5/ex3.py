""" Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7? """
n = 1067
count = 0
while n <= 3627:
    if n % 2 == 0:
        if n % 7 == 0:
            count += 1
    n += 1
print(count)