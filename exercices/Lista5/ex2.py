""" Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? (obs: na
nossa pseudo-linguagem, o laço inclui os extremos, ou seja, 1 até 4 significa 1, 2, 3, 4.)
para i = 1 até 9
    se i != 3, então
        para j = 1 até 6
            imprime 'oi' """
count = 0
j = 1
i = 1
while i <= 9:
    if i != 3:
        while j <= 6:
            print("Oi")
            count += 1
            j += 1
        j = 1
    i += 1
print(count)