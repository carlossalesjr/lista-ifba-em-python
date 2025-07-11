'''8. Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com
o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do
segundo).'''

def juntar_arquivos(arquivo1, arquivo2, arquivo_saida): 
    try:
        with open(arquivo1, 'r', encoding='utf-8') as f1, open(arquivo2, 'r', encoding='utf-8') as f2:
            conteudo1 = f1.read()
            conteudo2 = f2.read()
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f_saida:
            f_saida.write(conteudo1 + '\n' + conteudo2)
        
        print(f"Conteúdo dos arquivos '{arquivo1}' e '{arquivo2}' foi combinado em '{arquivo_saida}'.")
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

arquivo1 = input("Digite o caminho completo do primeiro arquivo: ")
arquivo2 = input("Digite o caminho completo do segundo arquivo: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")
juntar_arquivos(arquivo1, arquivo2, arquivo_saida)