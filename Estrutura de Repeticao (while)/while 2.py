#2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.

senha_correta = "coringao1010"

senha_usuario = input("Digite a senha: ")

while senha_usuario != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_usuario = input("Digite a senha: ")

print("Senha correta! Acesso permitido.")  
