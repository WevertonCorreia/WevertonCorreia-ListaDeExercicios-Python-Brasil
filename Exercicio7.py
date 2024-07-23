# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite a area do quadrado: "))
area = lado ** 2
dobro = 2 * area
print(f"A area do quadrado é {area:.2f}, o dobro da area é {dobro:.2f}")