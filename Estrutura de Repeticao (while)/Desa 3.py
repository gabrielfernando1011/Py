#3. Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.

numero = int(input("Digite um número inteiro: "))

contagem = 0

while True:
    numero = numero // 10
    contagem += 1

    if numero == 0:
        break

print(f"O número tem {contagem} dígitos.")  
