# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário
#digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

contador = 0
ultimo_numero = None

while True:
    numero = int(input("Digite um número: "))
    contador += 1 
    
    if numero == ultimo_numero:
        break 

    ultimo_numero = numero

print(f"Você inseriu {contador} números.") 