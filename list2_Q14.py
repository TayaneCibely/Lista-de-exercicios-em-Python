salario = float(input("Digite o valor do salário: "))
novo_salario = 0

if salario <= 300:
    novo_salario = salario*150/100
    print("O valor do seu novo salário é: ",novo_salario)
elif 300 < novo_salario >= 500:
    novo_salario = salario*140/100
    print("O valor do seu novo salário é: ",novo_salario)
elif 500 < novo_salario >= 700:
    novo_salario = salario*130/100
    print("O valor do seu novo salário é: ",novo_salario)
elif 700 < novo_salario >= 800:
    novo_salario = salario*120/100
    print("O valor do seu novo salário é: ",novo_salario)
elif 800 < novo_salario >= 1000:
    novo_salario = salario*110/100
    print("O valor do seu novo salário é: ",novo_salario)
else:
    novo_salario = salario*105/100
    print("O valor do seu novo salário é: ",novo_salario)
