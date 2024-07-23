# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.


primeiro_numero = int(input('Digite um número inteiro: '))
segundo_numero = int(input('Digite outro número inteiro: '))
numero_real = float(input('Digite um numero real: '))

resultado_a = (primeiro_numero * 2) * (segundo_numero / 2)
resultado_b = (3 * primeiro_numero) + numero_real
resultado_c = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado_a}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado_b}")
print(f"O terceiro elevado ao cubo é: {resultado_c}")