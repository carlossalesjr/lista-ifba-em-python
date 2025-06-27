'''14) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro
Escreva um programa em python algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pagopelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcoolé R$ 1,90.'''

litros_vendidos = float(input("Digite o número de litros vendidos: "))
while litros_vendidos < 0:
    print("O número de litros vendidos deve ser um valor positivo.")
    litros_vendidos = float(input("Digite o número de litros vendidos: ")) 
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()
while tipo_combustivel not in ['A', 'G']:
    print("Tipo de combustível inválido. Por favor, escolha A para álcool ou G para gasolina.")
    tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()
preco_alcool = 1.90
preco_gasolina = 2.50
if tipo_combustivel == 'A':
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_final = litros_vendidos * preco_alcool * (1 - desconto)
else:
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_final = litros_vendidos * preco_gasolina * (1 - desconto)
print(f"\nValor a ser pago pelo cliente: R$ {preco_final:.2f}")
