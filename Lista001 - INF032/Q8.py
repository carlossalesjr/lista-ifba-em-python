# 8. supondo um numero 123, imprimi-lo invertido. Exemplo (123, 321). O numero deverá ser armazenado em outra
# variável.

num = 123 
invertido = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)  

print("Número original:",  num)
print("Número invertido:", invertido)
