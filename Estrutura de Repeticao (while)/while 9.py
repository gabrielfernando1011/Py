# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos
#desejados. O programa deve calcular o valor total e permitir que o usuário finalize o
#pedido digitando 0.

produtos = {
    1: {'nome': 'Bala', 'preco': 10.0},
    2: {'nome': 'Chocolate', 'preco': 20.0},
    3: {'nome': 'Energetico', 'preco': 30.0},
    4: {'nome': 'Chiclete', 'preco': 40.0}}
while True:
    total_pedido = 0  
    print("Bem-vindo ao sistema de pedidos!")
    print("Códigos de produtos disponíveis:")
    
    for codigo, produto in produtos.items():
        print(f"Código: {codigo}, Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    
    while True:
        
        codigo_produto = int(input("Digite o código do produto desejado (ou 0 para finalizar o pedido): "))
        
        if codigo_produto == 0:
            
            print(f"Total do pedido: R${total_pedido:.2f}")
            break
        elif codigo_produto in produtos:
            
            quantidade = int(input(f"Quantos {produtos[codigo_produto]['nome']} você deseja? "))
            
            if quantidade > 0:
                
                total_pedido += produtos[codigo_produto]['preco'] * quantidade
                print(f"Você adicionou {quantidade} unidades de {produtos[codigo_produto]['nome']}.")
            else:
                print("Quantidade inválida! A quantidade deve ser maior que 0.")
        else:
            print("Código inválido! Por favor, insira um código válido.")
    
    continuar = input("Deseja fazer outro pedido? (s/n): ").strip().lower()
    
    if continuar != 's':
        print("Obrigado por fazer o pedido! Até logo!")
        break     