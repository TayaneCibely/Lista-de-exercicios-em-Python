salario = float(input("Digite seu salário: "))

if salario <= 300:
    aumento = salario*15/100
    novo_salario = salario*115/100
    print("O valor do aumento é: ",aumento,"\nE seu novo salário é: ",novo_salario)
elif 300 < salario <= 600:
    aumento = salario*10/100
    novo_salario = salario*110/100
    print("O valor do aumento é: ",aumento,"\nE seu novo salário é: ",novo_salario)
elif 600 < salario <=  900:
    aumento = salario*5/100
    novo_salario = salario*105/100
    print("O valor do aumento é: ",aumento,"\nE seu novo salário é: ",novo_salario)
else:
    print("Você não receberá aumento!:(")


    
