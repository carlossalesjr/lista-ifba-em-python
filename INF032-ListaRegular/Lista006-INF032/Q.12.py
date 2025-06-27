'''12) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.• 
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preço sem 3 situações:
• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o preço seja o menor. 

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
while area < 0:
    if area <= 0:
        print("A área deve ser um valor positivo.")

    cobertura_por_litro = 6
    litros_necessarios = area / cobertura_por_litro

    litros_por_lata = 18
    litros_por_galao = 3.6

    preco_lata = 80.00
    preco_galao = 25.00

    litros_necessarios *= 1.10

    latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
    custo_latas = latas_necessarias * preco_lata

    galaos_necessarios = math.ceil(litros_necessarios / litros_por_galao)
    custo_galoes = galaos_necessarios * preco_galao

    latas_mistas = math.floor(litros_necessarios / litros_por_lata)
    restante_litros = litros_necessarios - (latas_mistas * litros_por_lata)
    galaos_mistos = math.ceil(restante_litros / litros_por_galao)
    custo_misto = (latas_mistas * preco_lata) + (galaos_mistos * preco_galao)

    print(f"\nQuantidade de tinta necessária: {litros_necessarios:.2f} litros")
    print(f"1. Apenas latas de 18 litros: {latas_necessarias} lata(s) - Custo: R$ {custo_latas:.2f}")
    print(f"2. Apenas galões de 3,6 litros: {galaos_necessarios} galão(ões) - Custo: R$ {custo_galoes:.2f}")
    print(f"3. Misturando latas e galões: {latas_mistas} lata(s) e {galaos_mistos} galão(ões) - Custo: R$ {custo_misto:.2f}")

    