''' 9.Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. para cada consumidor, são digitados os seguintes dados:
a)Numero do consumidor; 
b)Quantidade de kWh consumidos durante o mês; 
c)tipo do consumidor -> 1-residencial, preço em reias de kWh = 0,3 / 2-comercial, preço em reias de kWh = 0,5 / 3-industrial, preço em reias de kWh = 0,7. 
Os dados devem ser lidos ate que seja encontrado um consumidor com numero 0(zero). calcular e imprimir:
 a) o custo total para cada consumidor; b)o total de consumo para os 3(três) tipos de consumidor; c)a media de consumo dos tipos 1 e 2.'''

total_consumo = {1: 0, 2: 0, 3: 0}
media_consumo = {1: 0, 2: 0}
num_consumidor = 1
cont1 = 0
cont2 = 0
while num_consumidor != 0:
    num_consumidor = int(input("Digite o número do consumidor (0 para sair): "))
    if num_consumidor == 0:
        break
    kWh = float(input("Digite a quantidade de kWh consumidos: "))
    tipo = int(input("Digite o tipo do consumidor: "))
    
    if tipo == 1:
        custo = kWh * 0.3
        total_consumo[1] += kWh
        cont1 += 1
    elif tipo == 2:
        custo = kWh * 0.5
        total_consumo[2] += kWh
        cont2 += 1
    elif tipo == 3:
        custo = kWh * 0.7
        total_consumo[3] += kWh
    else:
        print("Tipo inválido.")
        continue
    
    print(f"Custo total para o consumidor {num_consumidor}: R$ {custo:.2f}")
    print()

for tipo in total_consumo:
    print(f"Total de consumo para o tipo {tipo}: {total_consumo[tipo]} kWh")
print()    
for tipo in media_consumo:
    media_consumo[tipo] = total_consumo[tipo] / (cont1 if tipo == 1 else cont2)
    print(f"Média de consumo para o tipo {tipo}: {media_consumo[tipo]:.2f} kWh")
   

    
    
