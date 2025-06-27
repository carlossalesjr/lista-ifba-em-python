# 10.Criar umprograma que deixe entrar com 10 números positivos e imprima a raiz quadrada de cada numero.
#  para cada entrada de dados devera haver um trecho de "proteção" para que um numero negativo não seja aceito.

import math

numeros = []
num = 1
for i in range(10):
    while True:
        num = float(input(f"Digite um número positivo: "))
        if num < 0:
            print("Número negativo não é aceito. Tente novamente.")
        else:
            numeros.append(num)
            break

for numero in numeros:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")