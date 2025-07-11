'''1. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
linhas esse arquivo possui. '''

def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            print(f"O arquivo '{nome_arquivo}' possui {len(linhas)} linha(s).")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    nome_do_arquivo = input("Digite o caminho completo do arquivo de texto:")
    contar_linhas(nome_do_arquivo)