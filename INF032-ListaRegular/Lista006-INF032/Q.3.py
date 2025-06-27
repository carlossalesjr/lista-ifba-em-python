#3.Entrar com vários números positivos e imprimir a media dos números digitados.
#  o programa acaba quando se informar que não deseja mais continuar.

cont = 0.0
soma = 0
response = 'y'
while response == 'y':
    soma += int(input("Digite um número: "))
    cont += 1
    response = input("Deseja continuar? (y/n): ")

print(f"A média dos números digitados é {soma / cont}")