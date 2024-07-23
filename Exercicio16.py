"""
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math
metro = float(input('Digite o tamanho em metros quadrados da área que vai pintar: '))

cobertura_por_litro = 3
litros_por_lata = 18 
valor_da_lata = 80

litros_necessarios = metro / cobertura_por_litro


latas = math.ceil(litros_necessarios / litros_por_lata)

preco = latas * valor_da_lata
print(f'O numero de latas é : {latas}')
print(f'O valor a se pago é: R${preco:.2f}')


    

