''' 5. Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. Apresentar os
valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos. '''

consumo = 12
tempo = float(input("Digite o tempo gasto na viagem: "))
velocidade = float(input("Digite a velocidade média: "))

distancia = velocidade * tempo
litros = distancia / consumo

print(f"Velocidade média: {velocidade} km/h")
print(f"Tempo gasto: {tempo} horas")
print(f"Distância percorrida: {distancia} km")
print(f"Quantidade de litros gastos: {litros:.2f} litros")
