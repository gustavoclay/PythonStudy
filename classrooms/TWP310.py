archive = open('numbers.txt', 'w')
for linha in range(1, 101):
    archive.write('%d\n' %linha)
archive.close