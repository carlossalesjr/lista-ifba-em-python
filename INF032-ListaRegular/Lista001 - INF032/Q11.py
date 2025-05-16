'''
11. Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e
compraram alguns itens:
• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
• 2 pacotes de macarrão: R$ 8,73 cada
• 1 pacote de Molho de tomate: R$ 3,45
• 420g Cebola: R$ 5,40/kg
• 250g de Alho: R$ 30/kg
• 450g de pães franceses: R$ 25/kg

Calcule quanto ficou para cada um.
'''
cerveja = 75 * 2.20
macarrao = 2 * 8.73 
molho = 3.45
cebola = 0.420 * 5.40
alho = 0.250 * 30
paes = 0.450 * 25
total = cerveja + macarrao + molho + cebola + alho + paes

print("cada um vai pagar: ", total / 5)