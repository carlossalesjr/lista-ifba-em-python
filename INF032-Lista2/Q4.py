# 4. Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
# aulas dadas; c) percentual de desconto INSS.

ValorHora = float(input("Digite o valor da hora aula: "))
NumeroAulas = int(input("Digite o número de aulas dadas: "))
DescontoINSS = float(input("Digite o percentual de desconto do INSS: "))

SalarioBruto = ValorHora * NumeroAulas
Desconto = (DescontoINSS / 100) * SalarioBruto

SalarioLiquido = SalarioBruto - Desconto
print(f"Salário Bruto: R$ {SalarioBruto:.2f}")