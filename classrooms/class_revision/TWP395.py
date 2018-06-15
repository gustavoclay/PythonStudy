f = open('surf.txt')
higher_note = 0
for line in f:
    name, note = line.split()
    if float(note) > higher_note:
        higher_note = float(note)
f.close()

print(higher_note)