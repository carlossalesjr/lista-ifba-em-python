#2.Entrar com números enquanto forem positivos, e imprimir quantos números foram digitados;
cont = 0
num = int(input("Digite um número positivo (negativo para sair): "))

if (num > 0):
    while num > 0:
        cont += 1
        num = int(input("Digite um número positivo (negativo para sair): "))

print(f"Foram digitados {cont} números positivos.")