'''3. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais e quantas são consoantes.'''

def contar_vogais_consoantes(nome_arquivo):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    total_vogais = 0
    total_consoantes = 0

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for char in conteudo:
                if char in vogais:
                    total_vogais += 1
                elif char in consoantes:
                    total_consoantes += 1
            print(f"O arquivo possui:")
            print(f"- {total_vogais} vogais")
            print(f"- {total_consoantes} consoantes")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_do_arquivo = input("Digite o caminho completo do arquivo de texto: ")
contar_vogais_consoantes(nome_do_arquivo)