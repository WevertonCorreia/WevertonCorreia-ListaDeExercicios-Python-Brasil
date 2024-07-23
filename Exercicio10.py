# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_em_C = int(input("Digite a temperatura em celsius: "))
temperatura_em_F = temperatura_em_C * 1.8 + 32

print(f"A temperatura em celsius {temperatura_em_C:.2f}°C convertendo para Fahrenheit {temperatura_em_F:.2f}°F ")