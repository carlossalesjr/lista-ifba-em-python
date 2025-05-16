# 5. Quantos segundos há em 3 horas, 23 minutos e 17 segundos?
segsPorMinuto = 60
minutosPorHora = 60
horas = 3
minutos = 23
segundos = 17
totalSegundos = (horas * minutosPorHora * segsPorMinuto) + (minutos * segsPorMinuto) + segundos
print("Total de segundos:", totalSegundos)
