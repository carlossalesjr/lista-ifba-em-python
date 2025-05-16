'''7. Criar um programa que leia a quantidade de fitas de uma locadora de vídeo possui e o valor que ela cobra
por cada aluguel, mostrando as informações pedidas a seguir: a) sabendo que um terço das fitas são
alugadas por mês, exiba o faturamento anual da locadora; b)Quando o cliente atrasa a entrega, é cobrada
uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se
estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
que a locadora terá no final do ano.'''

qtdFitas = int(input("Digite a quantidade de fitas da locadora: "))
valorAluguel = float(input("Digite o valor do aluguel: "))

faturamentoAnual = (qtdFitas / 3) * valorAluguel * 12
multaMensal = (qtdFitas / 3) * valorAluguel * 0.10
qtdFitasEstragadas = qtdFitas * 0.02
qtdFitasReposicao = qtdFitas * 0.10
qtdFitasFinal = qtdFitas - (qtdFitas * 0.02) + (qtdFitas * 0.10)

print(f"Faturamento Anual: R$ {faturamentoAnual:.2f}")
print(f"Valor ganho com multas por mês: R$ {multaMensal:.2f}")
print(f"Quantidade de fitas que a locadora terá no final do ano: {qtdFitasFinal:.2f}")