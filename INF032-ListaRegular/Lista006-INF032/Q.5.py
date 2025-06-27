#5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de cada nome;

nome = input("Digite um nome (FIM para sair): ")
if nome != "FIM":
    while nome != "FIM":
        print(f"Primeiro caracter de {nome} é '{nome[0]}'")
        nome = input("Digite um nome (FIM para sair): ")
