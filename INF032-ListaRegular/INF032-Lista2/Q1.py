# 1. Entrar com dois números inteiros e imprimir a seguinte saída: a)dividendo; b) divisor; c) quociente; d) resto.

num1 = int(input("Digite o primeiro número inteiro (dividendo): "))
num2 = int(input("Digite o segundo número inteiro (divisor): "))

quociente = num1 // num2
resto = num1 % num2

print(f"Dividendo: {num1}")
print(f"Divisor: {num2}")   
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
