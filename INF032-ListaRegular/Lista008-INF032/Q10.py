'''10. Faça um programa no qual o usuario informa o nome do arquivo e uma palavra, e retorne
o numero de vezes que aquela palavra aparece no arquivo.'''

def contar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            contador = conteudo.lower().count(palavra.lower())
            return contador
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    
nome_arquivo = input("Digite o caminho completo do arquivo de texto: ")
palavra = input("Digite a palavra que deseja contar: ")
resultado = contar_palavra(nome_arquivo, palavra)
if resultado is not None:
    print(f"A palavra '{palavra}' aparece {resultado} vezes no arquivo '{nome_arquivo}'.")
    