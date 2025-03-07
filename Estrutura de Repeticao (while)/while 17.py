# 4 Peca para o usuario digitar uma senha. O programa so deve parar de pedir quando ele acertar a senha correta (exemplo "1234").
senha = "1234"
tentativa = input("Digite a senha:")

while senha != tentativa:
    print("Senha errada. Tente novamente")
    tentativa = input("Digite a senha:")

    print("Acesso autorizador!")
      
 