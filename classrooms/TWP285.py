'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o nome do mês por extenso'''
#split dos meses
meses = 'janeiro,fevereiro,março,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro'
meses = meses.split(',')
#progama
data = input("Digite uma data(dd/mm/aaaa): ")
data = data.split('/')
print("%s de %s de %s" %(data[0], meses[int(data[1]) - 1], data[2]))
