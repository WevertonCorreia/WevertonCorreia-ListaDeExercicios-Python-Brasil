
metro = float(input('Digite o tamanho em metros quadrados da área que vai pintar: '))

cobertura_por_litro = 6 
litros_por_lata = 18  
custo_por_lata = 80.00  
litros_por_galao = 3.6  
custo_por_galao = 25.00 


litros_necessarios = (metro / cobertura_por_litro) * 1.1


latas_necessarias = int(litros_necessarios / litros_por_lata)
if litros_necessarios % litros_por_lata != 0:
    latas_necessarias += 1
custo_total_latas = latas_necessarias * custo_por_lata


galoes_necessarios = int(litros_necessarios / litros_por_galao)
if litros_necessarios % litros_por_galao != 0:
    galoes_necessarios += 1
custo_total_galoes = galoes_necessarios * custo_por_galao


latas_combinado = int(litros_necessarios / litros_por_lata)
restante_litros = litros_necessarios % litros_por_lata

galoes_combinado = int(restante_litros / litros_por_galao)
if restante_litros % litros_por_galao != 0:
    galoes_combinado += 1

custo_total_combinado = (latas_combinado * custo_por_lata) + (galoes_combinado * custo_por_galao)

print(f"O número de latas é: {latas_necessarias} e o custo total é: R$ {custo_total_latas:.2f}")
print(f"O número de galões é: {galoes_necessarios} e o custo total é: R$ {custo_total_galoes:.2f}")
print(f"Combinando latas e galões, o número de latas é: {latas_combinado} e o número de galões é: {galoes_combinado}")
print(f"O custo total combinando latas e galões é: R$ {custo_total_combinado:.2f}")