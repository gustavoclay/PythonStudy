'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento'''
popula_a = 80000
popula_b = 200000
anos = 0
while popula_a < popula_b:
    popula_a += (popula_a/100) * 3
    popula_b += (popula_b/100) * 1.5
    anos += 1
print("População A:", popula_a)
print("População B:", popula_b)
print("Anos necessários para que a população do país A ultrapasse ou iguale a população do país B: ", anos)