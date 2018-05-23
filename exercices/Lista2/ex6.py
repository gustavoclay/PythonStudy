'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%  para  o  INSS  e  5%  para  o  sindicato,  faça  um  programa  que  nos  dê  o  salário  bruto,  quanto  pagou  ao  INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto -Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a.+ Salário Bruto : R$
b.-IR (11%) : R$
c.-INSS (8%) : R$
d.-Sindicato ( 5%) : R$
e.= Salário Liquido : R$'''

valor_hora = float(input("Valor/Hora: "))
horas_trabalhadas = int(input("Horas Trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = (salario_bruto/100) * 11
inss = (salario_bruto/100) * 8
sindicato = (salario_bruto/100) * 5
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("Salario Bruto: ", salario_bruto)
print("Imposto de Renda: ", ir)
print("INSS: ", inss)
print("Desconto Sindicato: ", sindicato)
print("Total de Descontos: ", descontos)
print("Salario Liquido: ", salario_liquido)