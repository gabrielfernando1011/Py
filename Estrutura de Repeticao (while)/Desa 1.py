#1. Escreva um programa que leia um número N e imprima todos os termos da sequência de
#Fibonacci até que o maior termo seja menor ou igual a N.

N = int(input("Digite um número N: "))

a, b = 0, 1

while True:
    if a > N:
        break
    print(a, end=' ')
    a, b = b, a + b 