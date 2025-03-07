#8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos.
#A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba
#o troco. Após isso, o programa deve reiniciar para um novo cliente.

while True:
    total_compra = 0  
    print("Bem-vindo à caixa registradora!")
    
    while True:
        valor_produto = float(input("Insira o valor do produto (ou 0 para finalizar a compra): "))
        
        if valor_produto == 0:
            break  
        elif valor_produto < 0:
            print("O valor do produto não pode ser negativo. Tente novamente.")
        else:
            total_compra += valor_produto  
    
    print(f"Total da compra: R${total_compra:.2f}")
    
    while True:
        valor_pago = float(input("Informe o valor pago pelo cliente: R$"))
        
        if valor_pago < total_compra:
            print("O valor pago é insuficiente. Tente novamente.")
        elif valor_pago == total_compra:
            print("O pagamento foi exato. Não há troco.")
            break  
        else:
            troco = valor_pago - total_compra
            print(f"Troco a ser devolvido: R${troco:.2f}")
            break  
    
    resposta = input("Deseja atender outro cliente? (s/n): ").strip().lower()
    
    if resposta != 's':
        print("Obrigado por usar a caixa registradora!") 
        break  