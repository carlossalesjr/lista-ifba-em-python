# 2. Entrar com quatro números e imprimir a media ponderada, sabendo-se que os pesos são respectivamente 1,2,3,4.

nota1 = float(input("Digite a primeira nota: "))
peso1 = 1   
nota2 = float(input("Digite a segunda nota: "))
peso2 = 2
nota3 = float(input("Digite a terceira nota: "))
peso3 = 3
nota4 = float(input("Digite a quarta nota: "))
peso4 = 4

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)
print(f"A média ponderada é: {media_ponderada:.2f}")