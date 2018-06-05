def epar(x):
    return x % 2 == 0

def fatorial(x):
    fat = 1
    while x > 1:
        fat = fat * x
        x = x - 1
    return fat