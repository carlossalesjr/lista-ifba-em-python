'''4. Faça um programa que receba do usuário um arquivo texto e um caráter. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.'''

def contar_caractere(nome_arquivo, caracter):
    contador = 0

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            contador = conteudo.count(caracter)
        print(f"O caractere '{caracter}' ocorre {contador} vez(es) no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_do_arquivo = input("Digite o caminho completo do arquivo de texto: ")
caracter = input("Digite o caractere que deseja contar: ")
contar_caractere(nome_do_arquivo, caracter)