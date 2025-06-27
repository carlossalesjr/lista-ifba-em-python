'''Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
radioativo. Sabendo-se que este perde 25% de sua massa a cada 30 segundos, criar um
programa que imprima o tempo necessário para que a massa deste material se torne
menor que 0,10 gramas. O programa pode calcular o tempo para várias massas.'''

while True:
    resposta = input("Deseja calcular o tempo para uma nova massa? (s/n): ")
    if resposta.lower() != 's':
        break
    massa = float(input("Digite a massa do material radioativo: "))
    tempo = 0

    while massa >= 0.10:
        massa *= 0.75 
        tempo += 30

    print(f"O tempo necessário para que a massa do material se torne menor que 0,10 gramas é: {tempo} segundos") 