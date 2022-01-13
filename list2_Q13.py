preco = float(input("Digite o preço do produto: "))

if preco <= 50:
    novo_preco = preco*105/100
    print("O novo preço do produto é: ",novo_preco)
elif 50 < preco <= 100:
    novo_preco = preco*110/100
    print("O novo preço do produto é: ",novo_preco)
else:
    novo_preco = preco*115/100
    print("O novo preço do produto é: ",novo_preco)
    

if novo_preco <= 80:
    print("O novo preço do produto é classificado como: Barato")
elif 80 < novo_preco <= 120:
    print("O novo preço do produto é classificado como: Normal")
elif 120 < novo_preco <= 200:
    print("O novo preço do produto é classificado como: Caro")
else:
    print("O novo preço do produto é classificado como: Muito Caro")
