codigo = int(input("Digite o código do produto comprado: "))
q = int(input("Digite a quantidade do produto que você quer comprar: "))


if 1<= codigo <=10:
    print("O preço unitário do produto é R$10,00")
    total_nota = q * 10
elif 11<= codigo <=20:
    print("O preço unitário do produto é R$15,00")
    total_nota = q * 15
elif 21<= codigo <=30:
    print("O preço unitário do produto é R$20,00")
    total_nota = q * 20
elif 31<= codigo <=40:
    print("O preço unitário do produto é R$30,00")
    total_nota = q * 30
    

if total_nota <=250:
    preco_final = total_nota*95/100
elif 250 < total_nota <=500:
    preco_final = total_nota*80/100
else:
    preco_final = total_nota*75/100

print("O preço total da nota é: ",total_nota,"\nCom o desconto o valor final fica: ",preco_final)
