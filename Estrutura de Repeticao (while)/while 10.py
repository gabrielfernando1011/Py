#10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo
#(5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de
#votos nulos e brancos. A entrada 0 encerra a votação.

votos_candidatos = [0, 0, 0, 0]  
votos_nulos = 0  
votos_brancos = 0  
total_votos = 0  

while True:
    print("Digite o número do seu voto:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Candidato 4")
    print("5 - Voto nulo")
    print("6 - Voto branco")
    print("0 - Encerrar votação")
    
    voto = int(input("Escolha uma opção: "))
    
    if voto == 1:
        votos_candidatos[0] += 1
        total_votos += 1
    elif voto == 2:
        votos_candidatos[1] += 1
        total_votos += 1
    elif voto == 3:
        votos_candidatos[2] += 1
        total_votos += 1
    elif voto == 4:
        votos_candidatos[3] += 1
        total_votos += 1
    elif voto == 5:
        votos_nulos += 1
        total_votos += 1
    elif voto == 6:
        votos_brancos += 1
        total_votos += 1
    elif voto == 0:
        break  
    else:
        print("Opção inválida. Tente novamente.")
        continue

print("\nResultados da votação:")
print(f"Candidato 1: {votos_candidatos[0]} votos")
print(f"Candidato 2: {votos_candidatos[1]} votos")
print(f"Candidato 3: {votos_candidatos[2]} votos")
print(f"Candidato 4: {votos_candidatos[3]} votos")
print(f"Votos nulos: {votos_nulos} votos")
print(f"Votos brancos: {votos_brancos} votos")
print(f"Total de votos: {total_votos}")

if total_votos > 0:
    porcentagem_nulos = (votos_nulos / total_votos) * 100
    porcentagem_brancos = (votos_brancos / total_votos) * 100
    print(f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%")
    print(f"Porcentagem de votos brancos: {porcentagem_brancos:.2f}%")
else:
    print("Nenhum voto registrado.") 