#7. Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias

idade = int(input("qual sua idade em dias? "))
anos = int(idade/365)
meses = int((idade%365) / 30)
dias = int((idade%365) % 30)

print ("voce viveu", anos, "anos,", meses, "meses e", dias, "dias")
