#1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse numero.      

numero = int(input("Digite um número inteiro positivo: "))

contador = 2

if numero > 0:
    print("Números pares de 2 até", numero, ":")
    
    while contador <= numero:
        print(contador)
        contador += 2
else:
    print("Por favor, digite um número inteiro positivo.")   