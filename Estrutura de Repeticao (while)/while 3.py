#3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o
#usuário digite -1. Em seguida, exiba a média das notas.

soma_notas = 0
contador = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): "))
    
    if nota == -1:
        break
    
    soma_notas += nota
    contador += 1

if contador > 0:
    
    media = soma_notas / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")  
