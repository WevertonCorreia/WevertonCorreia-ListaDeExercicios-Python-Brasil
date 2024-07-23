# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

validacao = str(input("Se for homen digite (H), se for mulher digite (M): ")).upper()

if validacao == "H":
    altura = float(input("Digite sua altura:"))
    calculo = (72.7*altura) - 58
    print (f"O peso ideal é: {calculo:.2f}")
else:
    validacao == "M"
    altura = float(input("Digite sua altura:"))
    calculo = (62.1*altura) - 44.7
    print (f"O peso ideal é: {calculo:.2f}")
