#C:\Users\kkjun\Faculdade\lista-ifba-em-python\INF032-ListaRegular\Lista008-INF032\teste.txt
'''5. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.'''

def contar_letras(nome_arquivo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    contador_letras = {letra: 0 for letra in alfabeto}

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            for char in conteudo:
                if char in alfabeto:
                    contador_letras[char] += 1

        print("Contagem de letras no arquivo:")
        for letra, count in contador_letras.items():
            print(f"{letra}: {count}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_do_arquivo = input("Digite o caminho completo do arquivo de texto: ")
contar_letras(nome_do_arquivo)