'''8)Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda. 
Exemplo: uf é prefixo de ufabc. ufabc não é prefixo de uf.'''

def eh_prefixo(prefixo, palavra):
    if len(prefixo) > len(palavra):
        return False
    elif prefixo == palavra[:len(prefixo)]:
        return True
    
def menu():
    prefixo = input("Digite a primeira palavra (prefixo): ")
    palavra = input("Digite a segunda palavra: ")
    
    if eh_prefixo(prefixo, palavra):
        print(f"{prefixo} é prefixo de {palavra}.")
    else:
        print(f"{prefixo} não é prefixo de {palavra}.")

while True:
    menu()
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break