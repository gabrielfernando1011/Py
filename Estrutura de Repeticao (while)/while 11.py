#10. Apenas aceitar números positivos. O programa deve continuar pedindo
#um número até o usuário digitar um número positivo.



num = -1

while num <= 0:
    num = float(input("Digite um número positivo: "))
    if num <= 0:
        print("Número inválido. Tente novamente.")

print(f"Você digitou o número positivo: {num}")  