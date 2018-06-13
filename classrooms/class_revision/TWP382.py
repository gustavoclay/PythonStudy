import urllib.request
pagina = urllib.request.urlopen('https://www.ime.usp.br/~pf/algoritmos/aulas/unicode.html')
texto = pagina.read().decode('utf-8')
print(texto)

import antigravity
