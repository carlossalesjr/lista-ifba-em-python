'''Faça um programa que calcule o menor número possível de notas (cédulas) que um
valor, inserido pelo usuário, pode ser decomposto. As notas consideradas são de 100,
50, 20, 10, 5, 2 e 1.'''

valor = int(input("Digite o valor: "))
notas = [100, 50, 20, 10, 5, 2, 1]
resultado = []

for nota in notas:
    quantidade = valor // nota
    resultado.append(quantidade)
    valor -= quantidade * nota

print("Notas necessárias:")
for i in range(len(notas)):
    if resultado[i] > 0:
        print(f"{resultado[i]} nota(s) de R${notas[i]}")    