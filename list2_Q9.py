saldo_medio = float(input("Digite seu saldo médio no último ano: "))

if saldo_medio > 400:
    credito = saldo_medio * 3/10
    print("O valor do seu saldo médio é: ",saldo_medio, "\nO valor do seu crédito especial é: ",credito)
elif  300 < saldo_medio <= 400:
    credito = saldo_medio * 25/100
    print("O valor do seu saldo médio é: ",saldo_medio, "\nO valor do seu crédito especial é: ",credito)
elif 200 < saldo_medio <= 300:
    credito = saldo_medio * 20/100
    print("O valor do seu saldo médio é: ",saldo_medio, "\nO valor do seu crédito especial é: ",credito)
else:
    credito = saldo_medio * 10/100
    print("O valor do seu saldo médio é: ",saldo_medio, "\nO valor do seu crédito especial é: ",credito)
