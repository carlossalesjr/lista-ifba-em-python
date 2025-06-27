#8.Chico tem 1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3 cm por ano. 
# construir um programa que calcule e imprima quantos anos serão necessários para Juca seja maior que Chico;

chico = 150  
juca = 110
anos = 0

while juca <= chico:
    chico += 2
    juca += 3
    anos += 1
    
print(f"Serão necessários {anos} anos para que Juca seja maior que Chico.")