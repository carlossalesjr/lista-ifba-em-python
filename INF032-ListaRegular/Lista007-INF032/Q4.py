'''4)Um número é dito perfeito quando ele é igual a soma de seus fatores.
Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. 
Escreva uma função que recebe um inteiro e dizer se é perfeito ou não. 
Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.'''

def eh_perfeito(num):
    if num < 1:
        return False
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma == num

def numeros_perfeitos_ate(n):
    perfeitos = []
    for i in range(1, n + 1):
        if eh_perfeito(i):
            perfeitos.append(i)
    return perfeitos

def menu():
    choice = input("Digite 1 para verificar se um número é perfeito ou 2 para listar números perfeitos até n: ")
    if choice == '1':
        num = int(input("Digite um número inteiro: "))
        if eh_perfeito(num):
            print(f"{num} é um número perfeito.")
        else:
            print(f"{num} não é um número perfeito.")
    elif choice == '2':
        n = int(input("Digite um inteiro n: "))
        perfeitos = numeros_perfeitos_ate(n)
        print(f"Números perfeitos até {n}: {perfeitos}")
    else:
        print("Opção inválida. Tente novamente.")

while True:
    menu()
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break