#2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
#palíndromo (ou seja, se lido de trás para frente continua igual).

numero = int(input("Digite um número inteiro positivo: "))

numero_str = str(numero)

inicio = 0
fim = len(numero_str) - 1

while inicio < fim:
    if numero_str[inicio] != numero_str[fim]:
        print("O número NÃO é um palíndromo.")
        break
    inicio += 1
    fim -= 1
else:
    print("O número é um palíndromo.") 