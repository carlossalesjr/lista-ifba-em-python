# 7. uma figura cujo ângulo e 80 graus. Imprima o seno, co-seno, tangente, secante, cp-secante, e co-tangente.
import math

angulo = 80
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
secante = 1 / coseno
cosecante = 1 / seno
cotangente = 1 / tangente

print("Seno:", seno)
print("Coseno:", coseno)
print("Tangente:", tangente)
print("Secante:", secante)
print("Cosecante:", cosecante)
print("Cotangente:", cotangente)