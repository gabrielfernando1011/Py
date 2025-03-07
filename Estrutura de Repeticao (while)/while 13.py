#8. Encontrando o maior número inserido pelo usuário. Peça números ao
#usuário e, ao digitar 0, exiba o maior número inserido.

        
maior_numero = float('-inf')

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    if numero > maior_numero:
        maior_numero = numero

print("O maior número inserido foi:", maior_numero) 
    