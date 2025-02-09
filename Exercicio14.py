"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""

peso = float(input("Digite o peso do peixe pescado: "))

peso_limite = 50

if peso > peso_limite:
    excesso = peso - peso_limite
    multa = excesso * 4.00
    print(f"A excessão de peso foi {excesso:.2f} quilos")
    print(f'A multa a ser paga é de {multa:.2f}')

else:
    print("Não passou do excesso de peso. Sem multa a pagar")