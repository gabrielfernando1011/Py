#7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
#um número até acertar. (Declare um valor e receba outro)

numero_secreto = (8)
tentativa = int(input("Tente adivinhar o numero secreto de 1 a 10:"))
while tentativa != numero_secreto:

 tentativa = int(input("Errou! Tente novamente:"))
print("Voce acertou o numero secreto!")  
        