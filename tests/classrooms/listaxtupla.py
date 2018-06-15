from sys import getsizeof

print('Lista')
exemplo = []
for number in range(21):
    exemplo.append(number)
    print(getsizeof(exemplo), exemplo)
print('Tupla')
for number in range(21):
    exemplo = tuple(range(number))
    print(getsizeof(exemplo), exemplo)
