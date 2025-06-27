# 7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao ano,
# e um pais B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano. 
# calcular e imprimir o tempo necessário para que a população do pais A ultrapasse a população do pais B;

pais_A = 5000000
pais_B = 7000000
anos = 0

while pais_A <= pais_B:
    pais_A += int(pais_A * 0.03)
    pais_B += int(pais_B * 0.02)
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")