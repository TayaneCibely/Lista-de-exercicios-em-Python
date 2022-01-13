preco = float(input("Digite o preço do produto: "))
print("Escolha a categoria: 1-Limpeza, 2-Alimentação ou 3-Vestuário ")
categoria = int(input())
print("Escolha situação: R-Produto que necessitam de Refrigeração e N-Produtos que não necessitam de refrigeração. ")
situacao = input()
aumento = 0

if preco <= 25:
    if categoria==1:
        aumento = preco*5/100
    elif categoria==2:
        aumento = preco*8/100
    elif categoria==3:
        aumento = preco*10/100
else:
    if  categoria==1:
        aumento = preco*12/100
    elif categoria==2:
        aumento = preco*15/100
    elif categoria==3:
        aumento = preco*18/100

if categoria==2 and situacao=='R':
    novo_preco = preco+aumento-(preco*5/100)
    print("O valor do aumento é de: ",aumento,"\nO novo preço do produto é: ",novo_preco)
else:
    novo_preco = preco+aumento-(preco*8/100)
    print("O valor do aumento é de: ",aumento,"\nO novo preço do produto é: ",novo_preco)


if novo_preco <= 50:
    classificacao = 'Barato'
    print("O novo preço é classificado como: ",classificacao)
elif 50<= novo_preco <= 120:
    classificacao = 'Normal'
    print("O novo preço é classificado como: ",classificacao)
else:
    classificacao = 'Caro'
    print("O novo preço é classificado como: ",classificacao)

    
    
        
