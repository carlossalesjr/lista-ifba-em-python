'''7)Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.'''

def contar_letra(string, letra):
    contador = 0
    for char in string:
        if char.lower() == letra.lower():
            contador += 1
    return contador

def menu():
    string = input("Digite uma string: ")
    letra = input("Digite a letra que deseja contar: ")
    quantidade = contar_letra(string, letra)
    print(f"A letra '{letra}' aparece {quantidade} vezes na string.")

while True:
    menu()
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break