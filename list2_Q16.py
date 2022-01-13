preco = float(input("Digite o preço atual do produto: "))
codigo = int(input("Digite o código do produto: "))

if preco <=30:
    desconto = 0
    novo_preco = preco
    print("O preço do produto era: ",preco,"\nO valor do desconto é: ",desconto,"\nO novo preço do produto é: ",novo_preco)
elif 30 < preco <= 100:
    desconto = preco*110/100
    novo_preco = preco*110/100
    print("O preço do produto era: ",preco,"\nO valor do desconto é: ",desconto,"\nO novo preço do produto é: ",novo_preco)
else:
    desconto = preco*115/100
    novo_preco = preco*115/100
    print("O preço do produto era: ",preco,"\nO valor do desconto é: ",desconto,"\nO novo preço do produto é: ",novo_preco)

