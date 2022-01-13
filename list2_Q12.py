salario = float(input("Digite seu salário: "))

if salario <= 350:
    novo_salario = salario + 100 - (salario*7/100)
    print("O seu novo salário é: ",novo_salario)
elif 350 < salario <= 600:
    novo_salario = salario + 75 - (salario*7/100)
    print("O seu novo salário é: ",novo_salario)
elif 600 < salario <=  900:
    novo_salario = salario + 50 - (salario*7/100)
    print("O seu novo salário é: ",novo_salario)
else:
    novo_salario = salario + 35 - (salario*7/100)
    print("O seu novo salário é: ",novo_salario)
