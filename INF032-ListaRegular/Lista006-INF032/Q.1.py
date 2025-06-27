# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;

while num != 999:
    num = int(input("Digite um número (999 para sair): "))
    if num != 999:
        print(f"O triplo de {num} é {num * 3}")