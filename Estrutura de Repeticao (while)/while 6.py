#6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até
#que o usuário informe um valor válido.

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida! A nota deve estar entre 0 e 10.")

print(f"Nota válida: {nota}")  