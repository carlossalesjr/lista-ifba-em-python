from datetime import datetime

def calcular_idade(data_nascimento, data_hoje):
    idade = data_hoje.year - data_nascimento.year - \
            ((data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def processar_idades(arquivo_entrada, arquivo_saida):
    try:
        data_hoje_str = input("Digite a data de hoje (DD MM AAAA): ")
        data_hoje = datetime.strptime(data_hoje_str, "%d %m %Y")

        with open(arquivo_entrada, 'r', encoding='utf-8') as f_entrada, \
             open(arquivo_saida, 'w', encoding='utf-8') as f_saida:

            for linha in f_entrada:
                partes = linha.strip().split()
                if len(partes) < 4:
                    continue

                try:
                    nome = " ".join(partes[:-3])
                    dia = int(partes[-3])
                    mes = int(partes[-2])
                    ano = int(partes[-1])

                    data_nascimento = datetime(ano, mes, dia)
                    idade = calcular_idade(data_nascimento, data_hoje)

                    f_saida.write(f"{nome}: {idade} anos\n")

                except (ValueError, IndexError):
                    print(f"Aviso: Ignorando linha mal formatada: '{linha.strip()}'")
                    continue

        print(f"Arquivo de idades '{arquivo_saida}' foi criado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{arquivo_entrada}' não foi encontrado.")
    except ValueError:
        print("Erro: Formato de data inválido. Use DD MM AAAA.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


nome_entrada = input("Digite o nome do arquivo de entrada (nascimentos): ")
nome_saida = input("Digite o nome do arquivo de saída (idades): ")
processar_idades(nome_entrada, nome_saida)