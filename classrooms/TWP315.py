archive = open('numbers.txt', 'r')
for linha in archive.readlines():
    print(linha.rstrip())
archive.close()

with open('numbers.txt') as f:
    print(f.read())