preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite o código do produto: "))

if codigo==1:
    origem = 'Sul'
elif codigo==2:
    origem = 'Norte'
elif codigo==3:
    origem = 'Leste'
elif codigo==4:
    origem = 'Oeste'
elif codigo==5 or 6:
    origem = 'Nordeste'
elif codigo==7 or 8 or 9:
    origem = 'Sudeste'
elif 10 <= codigo <= 20:
    origem = 'Centro-Oeste'
elif 21 <= codigo <=30:
    origem = 'Nordeste'    

print("A origem do produto é: ",origem)
