# Calcule a média de 5 notas quaisquer
notas = [6, 7, 8, 4, 6]
media = 0
count = 0
while count < 5:
    media += notas[count]
    count += 1
media = media / len(notas)
print(media)