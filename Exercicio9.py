#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperatura_em_F = int(input("Digite a temperatura em Fahrenheit: "))
temperatura_em_C = 5 * ((temperatura_em_F - 32 )/9)

print(f"A temperatura em Fahrenheit {temperatura_em_F}°F convertendo para celsius {temperatura_em_C:.2f}°C")