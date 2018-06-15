archive_notes = open('surf.txt')
notes = []
for line in archive_notes:
    name, note = line.split()
    notes.append(float(note))
archive_notes.close()
notes.sort()
notes.reverse()
print(notes)