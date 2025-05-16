# 6. Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?

segsPorMinuto = 60
minutosPorHora = 60
horas = 3
minutos = 23
segundos = 17
totalSegundos = (horas * minutosPorHora * segsPorMinuto) + (minutos * segsPorMinuto) + segundos

km = 65
kmParaM = 1000
distanciaEmMetros = km * kmParaM

velocidadeMedia = distanciaEmMetros / totalSegundos
print("A velocidade média é de", velocidadeMedia, "m/s")