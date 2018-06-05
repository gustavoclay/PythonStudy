'''Verifique se uma palavra é palíndrome'''
palavra = input("Digite uma palavra:")
if palavra == palavra[::-1]:
    print("Palavra palíndrome")
else:
    print("Palavra não palíndrome")