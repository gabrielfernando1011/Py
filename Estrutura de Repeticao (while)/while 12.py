#9. Contar quantos números pares o usuário digitar. O programa deve
#contar quantos números pares o usuário inseriu. O usuário para
#digitando -1.


contador_pares = 0

while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    
    if numero == -1:
        break
    
    if numero % 2 == 0:
        contador_pares += 1

print("Você digitou", contador_pares, "números pares.")  
