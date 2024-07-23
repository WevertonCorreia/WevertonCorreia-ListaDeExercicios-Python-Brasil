"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

arquivo = float(input('Digite o tamanho do arquivo: '))
velocidade = float(input('Digite a velocidade da sua internet: '))

calculo = arquivo / (velocidade / 8)

minutos = calculo /60

print(f'O tempo aproximado para baixa o arquivo e de:{minutos:.2f} minutos!🕰 ')