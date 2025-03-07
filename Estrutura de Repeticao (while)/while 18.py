# 3 Peca para o usuario digitar numeros e some-os. O programa deve parar quando o usuario digitar 0.
num = int (input("Digite um numero"))
soma= 0 

while num != 0:
    soma += num
    num = int(input("Digite um numero (ou 0 para sair:)"))
    print(soma)
    
 