'''7. Desenvolver um programa que leia o conteúdo de um arquivo e cria um arquivo com o
mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os
nomes dos arquivos serão fornecidos, via teclado, pelo usuário.'''

def converter_maiusculas(nome_arquivo_entrada, nome_arquivo_saida):
    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
            conteudo = arquivo_entrada.read()
            conteudo_modificado = conteudo.upper()

        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(conteudo_modificado)

        print(f"Arquivo '{nome_arquivo_saida}' criado com sucesso, convertendo para maiúsculas.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo_entrada = input("Digite o caminho completo do arquivo de texto de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de texto de saída: ")
converter_maiusculas(nome_arquivo_entrada, nome_arquivo_saida)