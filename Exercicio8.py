# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Digite o valor que ganha por hora: '))
hora_trabalhada = float(input('Digite o valor horas trabalhada: '))
calculo = valor_hora * hora_trabalhada

print(f"Você vai receber R${calculo:.2f}")