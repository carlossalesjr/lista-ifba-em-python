# criar uma lista e imprimir
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)

# acessar o primeiro, o ultimo e um elemento no meio da lista
print(lista[0]) 
print(lista[-1]) 
print(lista[3]) 

#modificar e imprimir um elemento da lista
lista[6] = 10
print(lista)

#peça para o usuario um numero e adicione a lista
num = int(input("Digite um numero: "))
lista.append(num)
print(lista)

#remova algum elemento da lista
del lista[6]
print(lista)

#somar todos os elementos da lista
soma = 0
soma = sum(lista)
print(soma)

#criar uma lista desordanada e ordenar
lista2 = [10, 25, 12, 18, 20, 27, 8]
lista2.sort()
print(lista2)

#inverter a ordem da lista 1
lista.reverse()
print(lista)

#contar quantas vezes um elemento aparece na lista
cont = lista.count(10)
print(cont)

#fatiar a lista somente com os elementos do meio
lista3 = lista[1:5]
print(lista3)

#mesclar duas listas
lista4 = lista + lista2
print(lista4)

#verificar se um elemento existe na lista
print (10 in lista)
   
#remover elementos duplicados
lista5 = [1, 2, 3, 4, 5, 5]
lista5 = list(set(lista5))
print(lista5)

