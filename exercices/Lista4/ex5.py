''' Seja o mesmo texto acima(EX4) “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais. '''
def verifica(p):
    for c in 'python':
        if c in p and len(p) > 4:
            return True
    return False


texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'

import string
texto = texto.lower()
for c in string.punctuation:
    texto = texto.replace(c, ' ')
texto = texto.split()

count = 0
lista = []
for word in texto:
    if verifica(word):
        lista.append(word)
        count += 1

print(lista)
print(count)
