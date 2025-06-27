'''13) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg                  Acima de 5 Kg
File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
 Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
 contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

tipo_carne = input("Digite o tipo de carne (file, alcatra, picanha): ").strip().lower()
quantidade_kg = float(input("Digite a quantidade de carne em Kg: "))
while quantidade_kg < 0:
    print("A quantidade de carne deve ser um valor positivo.")
    quantidade_kg = float(input("Digite a quantidade de carne em Kg: "))
preco_por_kg = 0.0
if tipo_carne == "file":
    if quantidade_kg <= 5:
        preco_por_kg = 4.90
    else:
        preco_por_kg = 5.80
elif tipo_carne == "alcatra":
    if quantidade_kg <= 5:
        preco_por_kg = 5.90
    else:
        preco_por_kg = 6.80
elif tipo_carne == "picanha":
    if quantidade_kg <= 5:
        preco_por_kg = 6.90
    else:
        preco_por_kg = 7.80
else:
    print("Tipo de carne inválido. Por favor, escolha entre file, alcatra ou picanha.")
    exit()
total_compra = quantidade_kg * preco_por_kg
pagamento = input("Digite o tipo de pagamento (dinheiro, cartao): ").strip().lower()
desconto = 0.0
if pagamento == "cartao":
    desconto = total_compra * 0.05
    total_compra -= desconto
print("\nCupom Fiscal:")
print(f"Tipo de Carne: {tipo_carne.capitalize()}")
print(f"Quantidade: {quantidade_kg} Kg")
print(f"Preço Total: R$ {total_compra:.2f}")
print(f"Tipo de Pagamento: {pagamento.capitalize()}")
print(f"Valor do Desconto: R$ {desconto:.2f}" if desconto > 0 else "Sem desconto")
print(f"Valor a Pagar: R$ {total_compra:.2f}")
