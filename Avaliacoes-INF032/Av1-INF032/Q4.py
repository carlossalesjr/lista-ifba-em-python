'''Faça um programa que recebe uma string do usuário e informa se ela é um palíndromo.
Um palíndromo é uma frase que, excluindo os espaços em branco, pode ser lida
indiferentemente da esquerda para a direita e da direita para a esquerda. Alguns
palíndromos conhecidos são: ovo, radar, a grama é amarga, a base to teto desaba.'''

frase = input("Digite uma frase: ")

frase = frase.replace(" ", "").lower()

if (frase == frase[::-1]) == True:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")