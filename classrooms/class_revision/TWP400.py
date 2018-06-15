f = open('surf.txt')
notes = {}
for line in f:
    name, note = line.split()
    notes[float(note)] = name
f.close()
for note in sorted(notes, reverse=True):
    print('%s tem nota %4.2f' %(notes[note], note))
