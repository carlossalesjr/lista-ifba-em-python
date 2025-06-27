# 6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir seus divisores;

num = int(input("Digite um número (999 para sair): "))
while num != 999:
    print(f"Divisores de {num}: \n")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
    print()
    num = int(input("Digite um número (999 para sair): "))