'''Sabendo-se que a UAL calcula a divisão através de subtrações sucessivas, criar m
programa que calcule e imprima o resto da divisão de números inteiros lidos. suponha
que os números lidos sejam positivos e que o dividendo seja maior que o divisor.'''

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

aux = dividendo

while aux >= divisor:
    aux -= divisor

print(f"O resto da divisão de {dividendo} por {divisor} é: {aux}")
