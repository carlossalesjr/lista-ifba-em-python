''' 8. Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da
seguinte maneira. Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767.
Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. O
ultimo digito desse resultado é o digito verificador da conta (40-> 0 )'''

numeroConta = int(input("Digite o número da conta corrente (3 dígitos): "))

inverso = int(str(numeroConta)[::-1])
soma = numeroConta + inverso
numeroVerificador = (soma % 10 * 3) + (soma % 100 // 10 * 2) + (soma // 100 * 1)
digitoVerificador = numeroVerificador % 10

print(f"O dígito verificador da conta {numeroConta} é: {digitoVerificador}")