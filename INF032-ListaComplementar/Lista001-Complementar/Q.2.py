import math
# 1. Usar a biblioteca correta e as funções matemáticas do Python, quando necessárias,
# para resolver as seguintes expressões:

x = 3
y = 6

# a) w = e elevado a x - ln(y)
w = math.e**x - math.log(y)
print("a) w =", w)

# b) z = x*yelevado a 2 + y*cos(x)
z = x * (y**2) + y * math.cos(x)
print("b) z =", z)

#c) s = raiz  de (x/y + ln(x+y) + tan(x))
s = math.sqrt(x/y + math.log(x+y) + math.tan(x))
print("c) s =", s)
