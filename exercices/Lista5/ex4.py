""" Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos? """
n = 18644
count = 0
while n <= 33087:
    x = str(n)
    list(x)
    if '2' in x:
        if '7' not in x:
            count += 1
    n += 1
print(count)