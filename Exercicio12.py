#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite sua altura: "))
calculo =  (72.7*altura) - 58
print (f"O peso ideal é: {calculo:.2f}")