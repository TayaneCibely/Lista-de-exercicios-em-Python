custo_fabrica = float(input("Digite o custo de fábrica para a produção do carro: "))

if custo_fabrica <= 12000:
    custo_consumo = custo_fabrica + (custo_fabrica* 5/100)
    print("O custo do carro é: ",custo_consumo)
elif 12000 <  custo_fabrica >= 25000:
    custo_consumo = custo_fabrica + (custo_fabrica*5/100) + (custo_fabrica*15/100)
    print("O custo do carro é: ",custo_consumo)
else:
    custo_consumo = custo_fabrica + (custo_fabrica*5/100) + (custo_fabrica*20/100)
    print("O custo do carro é: ",custo_consumo)
    
