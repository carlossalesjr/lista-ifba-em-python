# 6. Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
# calcule o valor da prestação.

valorEmprestimo = float(input("Digite o valor do empréstimo: "))
taxaJuros = float(input("Digite a taxa de juros ao mes: "))
quantidadeMeses = int(input("Digite a quantidade de meses: "))

prestacao = (valorEmprestimo * taxaJuros) / quantidadeMeses

print(f"Valor da prestação: R$ {prestacao:.2f}")