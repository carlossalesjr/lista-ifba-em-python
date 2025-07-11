'''2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais.'''

def contar_vogais(nome_arquivo):
    vogais = 'aeiouAEIOU'
    contador_vogais = 0
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            for char in conteudo:
                if char in vogais:
                    contador_vogais += 1
        print(f"O arquivo possui {contador_vogais} vogais.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


nome_do_arquivo = input("Digite o caminho completo do arquivo de texto:")
contar_vogais(nome_do_arquivo)