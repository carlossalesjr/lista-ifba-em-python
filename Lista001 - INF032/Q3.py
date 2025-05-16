# 3. Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber
# quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
aulasPorSemana = 2
semanasNoMes = 4
qtdMeses = 4
totalAulas = aulasPorSemana * semanasNoMes * qtdMeses
faltasMax = totalAulas * 0.25
print("ele pode faltar", faltasMax, "aulas")