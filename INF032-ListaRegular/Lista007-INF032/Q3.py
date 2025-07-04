'''3)Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. 
Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.'''

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 1
while n > 0:
    n = int(input("Digite um inteiro positivo: "))
    primos = []
    for i in range(1, n + 1):
        if eh_primo(i):
            primos.append(i)
    
    print(f"Os números primos de 1 até {n} são: {primos}")