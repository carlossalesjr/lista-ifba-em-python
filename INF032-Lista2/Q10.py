''' 10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
Qual o tamanho dessa frase? E qual o tamanho de cada palavra? '''

frase = "Python é muito legal"

frase.split()
palavra1 = frase.split()[0]
palavra2 = frase.split()[1]
palavra3 = frase.split()[2]
palavra4 = frase.split()[3]

print("Tamanho da frase:", len(frase))
print("Tamanho da palavra 1:", len(palavra1))
print("Tamanho da palavra 2:", len(palavra2))   
print("Tamanho da palavra 3:", len(palavra3))
print("Tamanho da palavra 4:", len(palavra4))