'''9. Faça um programa que receba como entrada o nome de um arquivo de entrada e outro
de saída. O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando
40 caracteres) e o seu numero de habitantes. O programa devera ler o arquivo de entrada
e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo
seu numero de habitantes.'''

def cidade_mais_populosa(nome_arquivo_entrada, nome_arquivo_saida):
    cidade_populosa = ""
    max_habitantes = 0

    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
            for linha in arquivo_entrada:
                partes = linha.strip().split()
                if len(partes) < 2:
                    continue
                cidade = ' '.join(partes[:-1]).strip()
                try:
                    habitantes = int(partes[-1])
                except ValueError:
                    continue
                
                if habitantes > max_habitantes:
                    max_habitantes = habitantes
                    cidade_populosa = cidade

        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(f"{cidade_populosa} {max_habitantes}\n")

        print(f"Arquivo '{nome_arquivo_saida}' criado com a cidade mais populosa: {cidade_populosa} com {max_habitantes} habitantes.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo_entrada = input("Digite o caminho completo do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
cidade_mais_populosa(nome_arquivo_entrada, nome_arquivo_saida)

