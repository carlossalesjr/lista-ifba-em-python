'''1) Escreva um programa que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. 
Para cada opção, crie uma função.
Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha uma opção:")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    
    choice = input("Digite 1 ou 2: ")
    
    if choice == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius}°C")
    else:
        print("Opção inválida. Tente novamente.")

while True:
    menu()
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break