'''11. Abra um arquivo texto, calcule e escreva o numero de caracteres, o numero de linhas e
o numero de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais
caracteres espaco, tabulac  ̃ao ou nova linha.'''

def analisar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            num_caracteres = len(conteudo)
            
            num_linhas = conteudo.count('\n') + 1

            palavras = conteudo.split()
            num_palavras = len(palavras)

            letras = {}
            for char in conteudo.lower():
                if char.isalpha() and char not in 'áéíóúãõç':
                    letras[char] = letras.get(char, 0) + 1
            
            print(f"Número de caracteres: {num_caracteres}")
            print(f"Número de linhas: {num_linhas}")
            print(f"Número de palavras: {num_palavras}")
            print("Ocorrência de cada letra:")
            for letra, contagem in sorted(letras.items()):
                print(f"{letra}: {contagem}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo = input("Digite o caminho completo do arquivo de texto: ")
analisar_arquivo(nome_arquivo)