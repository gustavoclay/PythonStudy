import urllib.request
pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
texto = pagina.read().decode('utf-8')
onde = texto.find('>$')
inicio = onde + 2
fim = inicio + 4
preco = float(texto[inicio:fim])
if preco < 4.74:
    print(preco)
print(preco)