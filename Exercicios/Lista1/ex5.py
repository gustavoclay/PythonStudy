# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar
p = float(input('Preço: '))
d = float(input('Desconto em %: '))
tp = (p / 100)*d
td = p - tp
print ('Valor desconto: ', tp)
print ('Valor a pagar: ', td)
