#4.Entrar com vários números e informar quantos números entre 100 e 200 foram digitados. 
# quando o valor 0 for digitado o programa deve encerrar;

cont = 0
num = int(input("Digite um número (0 para sair): "))
if num != 0:
    while num != 0:
        if 100 <= num <= 200:
            cont += 1
        num = int(input("Digite um número (0 para sair): "))

print(f"Foram digitados {cont} números entre 100 e 200.")