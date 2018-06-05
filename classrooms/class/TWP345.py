'''Word Count with Dictionaries'''
import string
arquivo = open('ebook_alice.txt', encoding="utf8")
texto = arquivo.read()
texto = texto.lower()
for c in string.punctuation:
    texto = texto.replace(c, ' ')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print('Alice aparece %s vezes' %dic['alice'])
print(dic)
arquivo.close()

# Ao tentar rodar o programa, retornou este erro devido ao encoding do arquivo, utilizar utf8 para abrir o arquivo

# Traceback (most recent call last):
#   File "c:\Users\TR520596\Documents\github\PythonStudy\PythonStudy\classrooms\TWP345.py", line 4, in <module>
#     texto = arquivo.read()
#   File "C:\Users\TR520596\AppData\Local\Programs\Python\Python36-32\lib\encodings\cp1252.py", line 23,
# in decode
#     return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 8763: character maps to <undefined>