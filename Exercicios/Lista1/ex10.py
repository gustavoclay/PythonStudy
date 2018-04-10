# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias
q = int(input('Quantidade de cigarros consumidos em 1 dia: '))
a = int(input('Quantidade de anos consumindo cigarros: '))
t = a * 365
t = t * q
t = t * 10
t = t / 60
t = t / 24

print ('Dias de vida perdidos: ', t )
