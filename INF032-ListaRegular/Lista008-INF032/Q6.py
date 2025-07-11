'''6. Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto
contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.'''

def substituir_vogais(nome_arquivo_entrada, nome_arquivo_saida):
    vogais = 'aeiouAEIOU'
    
    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
            conteudo = arquivo_entrada.read()
            conteudo_modificado = ''.join('*' if char in vogais else char for char in conteudo)

        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(conteudo_modificado)

        print(f"Arquivo '{nome_arquivo_saida}' criado com sucesso, substituindo as vogais por '*'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo_entrada = input("Digite o caminho completo do arquivo de texto de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de texto de saída: ")
substituir_vogais(nome_arquivo_entrada, nome_arquivo_saida)
