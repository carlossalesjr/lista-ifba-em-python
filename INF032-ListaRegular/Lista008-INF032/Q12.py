'''12. Faça um programa que permita que o usuario entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informacoes, uma por linha. O usuario finaliza a
entrada com ‘0’ para o telefone.'''

def cadastrar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            while True:
                nome = input("Digite o nome do contato (ou 'sair' para finalizar): ")
                if nome.lower() == 'sair':
                    break
                telefone = input("Digite o telefone do contato (ou '0' para finalizar): ")
                if telefone == '0':
                    break
                arquivo.write(f"{nome}, {telefone}\n")
        print(f"Contatos salvos no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo = input("Digite o nome do arquivo para salvar os contatos: ")
cadastrar_contatos(nome_arquivo)
