'''6) Escreva uma funcão em Python que recebe uma lista e retorna uma outra lista contendo apenas os elementos que aparecem duas ou mais vezes na lista de entrada na ordem crescente.
Exemplo:

reps([1,4,2,3,4,2,3,4])

reps[2,3,4]'''

def reps(lista):
    resultado = []
    for x in lista:
        if lista.count(x) >= 2 and x not in resultado:
            resultado.append(x)
    return sorted(resultado)

lista_exemplo = [1, 4, 2, 3, 4, 2, 3, 4]
resultado = reps(lista_exemplo)
print(f"{resultado}")
    