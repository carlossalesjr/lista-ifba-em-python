'''2) A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. 
O termo seguinte da sequência é obtido somando os dois anteriores. 
Faça uma script em Python que solicite um inteiro positivo ao usuário, n. 
Então uma função exibe todos os termos da sequência até o n-ésimo termo. 
Use recursividade.'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

n = 1
while n > 0:
    n = int(input("Digite um inteiro positivo: "))
    fib_sequence = fibonacci(n)
    print(f"A sequência de Fibonacci até o termo {n} é: {fib_sequence}")
